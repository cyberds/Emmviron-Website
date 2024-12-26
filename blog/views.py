from django.shortcuts import render

def blog_index(request):
    return render(request, 'blog/blog_home.html', {})
