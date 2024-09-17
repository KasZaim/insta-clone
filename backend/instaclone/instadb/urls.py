from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ToggleLike, start_page_view, get_posts


urlpatterns = [
    path('', start_page_view, name='index'),
    path('get_posts/', get_posts.as_view(),name='get_posts'),
    path('toggle_like/', ToggleLike.as_view(), name='toggle_like'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)