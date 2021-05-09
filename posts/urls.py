from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Создаётся роутер
router = DefaultRouter()
# Связываем URL с viewset, аналогично обычному path()
router.register('api/v1/users', UserViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# router.register('api/v1/comments', CommentViewSet)
# router.register('api/v1/posts', PostViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # В список добавляем новый path() с роутером.
    # Все зарегистрированные в router пути доступны в router.urls
    path('', include(router.urls)),
]