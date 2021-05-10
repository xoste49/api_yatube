from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import UserSerializer, PostSerializer
from rest_framework import viewsets, status, request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    # api/v1/posts/ (GET, POST)
    # api/v1/posts/{post_id}/ (GET, PUT(PATCH), DELETE)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def partial_update(self, request, pk=None):
        post = get_object_or_404(Post, pk=id)
        if post.author != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=id)
        if post.author != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
