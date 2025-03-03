from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Check if the request is an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        blogs_data = []
        for blog in page_obj:
            blogs_data.append({
                'title': blog.title,
                'slug': blog.slug,
                'content': blog.content,
                'published_on': blog.published_on,
            })
        return JsonResponse({'blogs': blogs_data})  # Return a JSON response

    return render(request, 'blog/blog_list.html', {'blogs': page_obj, 'default_image_url': 'https://ik.imagekit.io/s3jkgwyie/Emmviron%20New%20Website%20Files/0248dda7999db27f6579c77a06fee713_11zon.jpg?updatedAt=1740375929480'})

def blog_detail(request, slug):
    # Get the blog post by its slug
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
