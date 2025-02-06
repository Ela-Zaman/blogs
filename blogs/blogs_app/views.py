from django.shortcuts import render, redirect

from .models import Blog
from .forms import BlogForm, PostForm

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

def new_blog(request):
    """Add new blog."""
    if request.method != 'POST':
        #No data submitted create a blank form
        form = BlogForm()
    else:
        #POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs_app:blogs')
    #Display a blank or invalid form.
    context = {'form' : form}
    return render(request,'blogs_app/new_blog.html', context)

def new_post(request, blog_id):
    """Add new post for a particular blog"""
    blog= Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        form = PostForm()    
    else :
        #POST data submitted, process data
        form = PostForm(data=request.POST)  
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect("blogs_app:blog", blog_id = blog_id)
    #Display a blank or invalid form
    context ={'blog': blog, 'form': form}
    return render(request, 'blogs_app/new_post.html',context)



        
