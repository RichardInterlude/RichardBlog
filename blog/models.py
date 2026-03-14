from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from api.utils import unique_slug_generator


POST_STATUS = (
    ('draft','Draft'),
    ('published','Published'),
    ('archived','Archived')
)

class SlugModel(models.Model):
    slug = models.SlugField(max_length=255, unique = True , blank=True, null=True)

    class Meta:
        abstract = True

    def save(self,*args, **Kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **Kwargs)


class Post(SlugModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ManyToManyField('Tag')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images')
    status = models.CharField(max_length=50, choices=POST_STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.title

class Category(SlugModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank =True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank = True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.name
    

class Tag(SlugModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)

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