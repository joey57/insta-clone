from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('', views.index , name = 'index'),
  path('upload/',views.upload_picture, name='upload'),
  path('add_comment/<int:post_id>/',views.add_comment, name='add_comment'),
  path('post/<int:pk>/',views.view_post, name='view_post'),
  path('user_profile/<username>/',views.user_profile, name='user_profile'),
  path('follow/<int:id>/',views.follow, name='follow'),
  path('unfollow/<int:id>/',views.unfollow, name='unfollow'),
  path('search/',views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)