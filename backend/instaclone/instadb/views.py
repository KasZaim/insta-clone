import json
from django.http import JsonResponse
from django.shortcuts import render
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
            total_likes=Count('liked_by')
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
            'likes_count',
            'total_likes',
            'image'
        )
        
        posts_list = []
        for post in posts:
            
            images = post['image'].split(', ') if post['image'] else [] # Split the image field into a list of image paths
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
                'likes_count': post['total_likes'], 
                'liked_by_me': post['liked_by_me'],  
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
                post.likes_count-=1
            else:
                post.liked_by_me = True
                post.likes_count+=1

            post.save()
            return JsonResponse({
                'liked': post.liked_by_me,
                'likes_count': post.likes_count
            })

        except Posts.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
