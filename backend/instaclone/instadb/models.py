from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Posts(models.Model):
    user_profile=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description= models.CharField(blank=False, max_length=50)
    image= models.ImageField(upload_to='post_images/')
    description_headline=models.CharField(blank=False,max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    hashtags=models.CharField(blank=True, max_length=50, default="")

class Comments(models.Model):
    pass