from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"username = {self.username} /  ProfileIMG= {self.profile_image}"
    #one-to-many posts,comments
    class Meta:
        verbose_name= "User"

class Posts(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(blank=False, max_length=60, default="")
    image = models.TextField(blank=True, null=True)  
    description_headline = models.CharField(blank=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.CharField(blank=True, max_length=50, default="")
    liked_by = models.ManyToManyField(UserProfile, related_name='liked_posts', through='Likes')
    liked_by_me = models.BooleanField(default=False)
    total_likes = models.IntegerField(default=5)  
    # many-to-many Ein Post kann von vielen Benutzern geliked werden/Ein Benutzer kann viele Posts liken.

    class Meta:
        verbose_name= "Post"
        ordering=['user_profile']
        
    def __str__(self):
        return f"{self.user_profile.username} - {self.description_headline}"

class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name="comments", on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.user_profile.username} on the post{self.post.description_headline}"
    class Meta:
        verbose_name= "Comment"

class Likes(models.Model):#trough Posts
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.username} liked {self.post.description_headline}"
    class Meta:
        verbose_name= "Like"

