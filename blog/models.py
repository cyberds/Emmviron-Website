# models.py

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Tags(models.Model):
    name = models.CharField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    published_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    tags = models.ManyToManyField("Tags", verbose_name="tags")

    def save(self, *args, **kwargs):
        # Automatically create slug from the title
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_on']
