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
]