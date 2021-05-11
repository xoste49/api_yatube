from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
