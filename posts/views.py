from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Post
from .permission import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthorOrReadOnly]

    def list(self):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    """
    api/v1/posts/ (GET, POST):
    получаем список всех постов или создаём новый пост

    api/v1/posts/{post_id}/ (GET, PUT(PATCH), DELETE):
    получаем, редактируем или удаляем пост по id
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT(PATCH), DELETE):
    получаем, редактируем или удаляем комментарий по id

    api/v1/posts/{post_id}/comments/ (GET, POST): получаем список
    всех комментариев или создаём новый,
    передав id поста, который хотим прокомментировать
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
