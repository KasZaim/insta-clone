from django.utils import timezone
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Comments, Likes, Posts, UserProfile
from django.db.models import Count
from django.utils.dateformat import DateFormat


def start_page_view(request):
    return render(request, 'index.html')

class get_posts(View):
    def get(self, request):
        posts = Posts.objects.all().annotate(
            comments_count=Count('comments'),
            total_likes_count=Count('liked_by')
        ).values(
            'id',
            'user_profile__username',
            'user_profile__profile_image',
            'user_profile__id',
            'description',
            'description_headline',
            'hashtags',
            'created_at',
            'comments_count',
            'liked_by_me',
            'total_likes',
            'image'
        )
        
        posts_list = []
        for post in posts:
            
            images = post['image'].split(', ') if post['image'] else [] # Split the image field into a list of image paths
            # image_url = post['image'] if post['image'] else ""
            created_at = DateFormat(post['created_at']).format('d.m.Y')# formats the Date
            comments = get_comments_for_post(post['id'])
            
            post_data = {
                'id': post['id'],
                'user_profile__username': post['user_profile__username'],
                'user_profile__profile_image': post['user_profile__profile_image'],
                'user_profile__id': post['user_profile__id'],
                'description': post['description'],
                'description_headline': post['description_headline'],
                'hashtags': post['hashtags'],
                'created_at': created_at,
                'comments_count': post['comments_count'],
                'liked_by_me': post['liked_by_me'],
                'total_likes': post['total_likes'],
                'images': images,  
                'comments': comments  
            }
            posts_list.append(post_data)

        return JsonResponse(posts_list, safe=False)

def get_comments_for_post(post_id):
    comments = Comments.objects.filter(post_id=post_id).values(
        'user_profile__username',
        'user_profile__profile_image',
        'comment_text',
        'created_at'
    )
    return list(comments)

class ToggleLike(View):
    def post(self, request):
        data = json.loads(request.body)
        post_id = data.get('post_id')
        try:
            post = Posts.objects.get(id=post_id)

            if post.liked_by_me:
                post.liked_by_me = False
                post.total_likes -=1
            else:
                post.liked_by_me = True
                post.total_likes+=1
                
            post.save()
            return JsonResponse({
                'liked': post.liked_by_me,
                'likes_count': post.total_likes
            })

        except Posts.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)

class PostComment(View):
    def post(self, request):
        data = json.loads(request.body)
        post_id = data.get('post_id')
        comment_text=data.get('comment_text')
        username=data.get('user_profile__username')
        try:
            post = Posts.objects.get(id=post_id)
            user_profile = UserProfile.objects.get(username=username)
            comment=Comments.objects.create(
                post=post,
                user_profile=user_profile,
                comment_text=comment_text,
            )
            comments_count = Comments.objects.filter(post=post).count()
            return JsonResponse({
                'success': True,
                'message': 'Comment posted successfully',
                'comments_count': comments_count
            })

        except Posts.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        
class CreatePostView(View):
    def get(self, request):
        return render(request, 'create-post.html')

    def post(self, request):
        description_headline = request.POST.get('description_headline')
        description = request.POST.get('description')
        hashtags = request.POST.get('hashtags')
        image = request.FILES.get('image')

        user_profile = UserProfile.objects.get(username='JasminTasty') 

        post = Posts.objects.create(
            user_profile=user_profile,
            description_headline=description_headline,
            description=description,
            hashtags=hashtags,
            image=image,
            created_at=timezone.now()
        )

        return redirect('get_posts') 