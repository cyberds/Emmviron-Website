from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tags(models.Model):
    name = models.CharField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    read_duration = models.IntegerField(default=10, help_text="Enter the read duration in minutes")
    published_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    tags = models.ManyToManyField("Tags", verbose_name="tags")
    top_rated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Automatically create slug from the title
        if not self.slug:
            self.slug = slugify(self.title)

        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_on']

@receiver(post_save, sender=Blog)
def update_top_rated(sender, instance, **kwargs):
    if instance.top_rated and kwargs.get('created', False) is False:
        Blog.objects.filter(top_rated=True).exclude(id=instance.id).update(top_rated=False)