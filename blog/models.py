from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
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
        if self.top_rated:
            Blog.objects.filter(top_rated=True).exclude(id=self.id).update(top_rated=False)

        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_on']