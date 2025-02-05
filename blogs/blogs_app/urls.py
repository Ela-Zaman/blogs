"""Define URL patterns for blog App. """

from django.urls import path
from . import views

app_name ='blogs_app'

urlpatterns = [
    #Home page
    path("",views.index,name ='index'),
    #page that shows all blogs.
    path('blogs/',views.blogs,name ='blogs'),
    #Details for a single blog.
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    #Page for adding new blog
    path('new_blog/',views.new_blog, name='new_blog'),
    #Page for adding new posts
    path('new_post/<int:blog_id>/',views.new_post, name='new_post'),
    #Page for editing add post
    #path('edit_post/<int:post_id>/',views.edit_post, name = 'edit_post'),

]