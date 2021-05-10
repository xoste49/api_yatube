from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post
        read_only_fields = ('author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('author', 'post', 'created')