from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet

"""
+ api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост
+ api/v1/posts/{post_id}/ (GET, PUT(PATCH), DELETE): получаем, редактируем или удаляем пост по id
+ api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT(PATCH), DELETE): получаем, редактируем или удаляем комментарий по id
api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев или создаём новый, передав id поста, который хотим прокомментировать
"""

router = DefaultRouter()
router.register('api/v1/users', UserViewSet, basename='users')
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register('api/v1/posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
