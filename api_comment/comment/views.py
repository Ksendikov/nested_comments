from rest_framework import viewsets
from rest_framework.views import APIView, Response
from .models import Comment, Post
from .serializer import CommentSerializer, PostSerializer
from mptt.utils import get_cached_trees


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = get_cached_trees(Comment.objects.all())






