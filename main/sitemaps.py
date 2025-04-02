from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Blog

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'business_plan', 'contact']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.published_on

    def location(self, obj):
        return reverse('blog_detail', args=[obj.slug])