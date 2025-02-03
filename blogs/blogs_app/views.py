from django.shortcuts import render

from .models import Blog

# Create your views here.
def index(request):
    """The home page for blog"""

    return render(request,'blogs_app/index.html')

def blogs(request):
    "Show all blogs."
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request,'blogs_app/blogs.html',context)

def blog(request, blog_id):
    """Show a single Blog and all its posts"""

    blog = Blog.objects.get(id=blog_id)
    posts=blog.post_set.order_by('-date_added')
    context={'blog': blog, 'posts': posts}
    return render(request, 'blogs_app/blog.html', context)