from django.db import models


class UserProfile(models.Model):
    username = models.CharField(
        max_length=50, blank=False, null=False, unique=True)
    profile_image = models.ImageField(
        upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username


class Posts(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(blank=False, max_length=50)
    image = models.ImageField(upload_to='post_images/')
    description_headline = models.CharField(blank=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.CharField(blank=True, max_length=50, default="")

    def __str__(self):
        return f"{self.user_profile.username} - {self.description_headline}"

class comments(models.Model):
    post = models.ForeignKey(
        Posts, related_name="comments", on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.user_profile.username} on the post{self.post.description_headline}"
