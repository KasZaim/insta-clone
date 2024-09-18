from django.contrib import admin
from .models import UserProfile, Comments,Posts,Likes
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Comments)
admin.site.register(Posts)
admin.site.register(Likes)