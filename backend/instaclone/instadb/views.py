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
        current_user_profile_id = request.GET.get('user_profile_id') 
        posts = Posts.objects.all().annotate(
            comments_count=Count('comments'),
            likes_count=Count('likes')
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
            'likes_count',
            'image'
        )
        
        posts_list = []
        for post in posts:
            
            images = post['image'].split(', ') if post['image'] else [] # Split the image field into a list of image paths
            created_at = DateFormat(post['created_at']).format('d.m.Y')# formats the Date
            comments = get_comments_for_post(post['id'])
            
            liked_by_me = Likes.objects.filter(post_id=post['id'], user_profile_id=current_user_profile_id).exists()
            
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
                'likes_count': post['likes_count'],
                'liked_by_me': liked_by_me,  
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
        post_id = request.POST.get('post_id')
        user_profile_id = request.POST.get('user_profile_id')

        try:
            post = Posts.objects.get(id=post_id)
            user_profile = UserProfile.objects.get(id=user_profile_id)

            # Überprüfen, ob der Benutzer den Post bereits geliked hat
            if user_profile in post.liked_by.all():
                # Benutzer hat bereits geliked, also Like entfernen
                post.liked_by.remove(user_profile)
                post.liked_by_me = False
            else:
                # Benutzer hat noch nicht geliked, also Like hinzufügen
                post.liked_by.add(user_profile)
                post.liked_by_me = True
            post.save()

            # Zähle die Likes für den Post
            likes_count = post.liked_by.count()

            # JSON-Daten als Antwort zurückgeben
            return JsonResponse({'liked': post.liked_by_me, 'likes_count': likes_count})

        except Posts.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'User profile not found'}, status=404)
