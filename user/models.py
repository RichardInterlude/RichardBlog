from django.db import models
from django.contrib.auth.models import User
import uuid


CHOICES_ROLE = (
    ('admin', 'Admin'),
    ('editor', 'Editor'),
    ('author', 'Author'),
    ('contributor', 'Contributor'),
    ('subscriber', 'Subscriber'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.SlugField()
    bio = models.TextField()
    # profile_pix = models.ImageField(upload_to='profile_pics/', blank = True, null = True)
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=50, choices=CHOICES_ROLE)
    social_media = models.URLField()

    def __str__(self):
        return self.user.username
