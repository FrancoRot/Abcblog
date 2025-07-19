from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='profile', null=True, blank=True)
    profession = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    birthday = models.DateField(null=True)
    twitter = models.URLField(max_length=50, null=True, blank=True)
    linkedin = models.URLField(max_length=50, null=True, blank=True)
    facebook = models.URLField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
    def __str__(self):
        return self.user.username
      


