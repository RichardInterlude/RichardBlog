from django.db import models
from django.contrib.auth.models import User


POST_STATUS = (
    ('draft','Draft'),
    ('published','Published'),
    ('archived','Archived')
)


class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ManyToManyField('Tag')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=POST_STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__ (self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'