from django.db import models


class Blog(models.Model):
    """Blog"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a name of a blog"""
        return self.title

class Post(models.Model):
    
    blog= models.ForeignKey(Blog, on_delete = models.CASCADE)
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name_plural = 'posts'
    def __str__(self):
        "Return a simple string representing the post. "
        return f"{self.text[:50]}..."
