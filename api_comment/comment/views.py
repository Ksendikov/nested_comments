from rest_framework import viewsets, mixins
from .models import Comment, Post
from .serializer import CommentSerializer, PostSerializer, AllCommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if self.get_object().level < 3:
                return CommentSerializer
        return AllCommentSerializer











