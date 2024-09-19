from django.contrib import admin
from .models import UserProfile, Comments,Posts,Likes
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['username', 'profile_image']
    
class CommentsAdmin(admin.ModelAdmin):
    list_display=['user_profile', 'comment_text','created_at']
    
class PostAdmin(admin.ModelAdmin):
    list_display=['user_profile', 'description_headline']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Posts,PostAdmin)
admin.site.register(Likes)