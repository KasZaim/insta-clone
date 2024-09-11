from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Posts(models.Model):
    description= models.CharField(blank=False, max_length=50)
    image= models.ImageField(upload_to=None)
