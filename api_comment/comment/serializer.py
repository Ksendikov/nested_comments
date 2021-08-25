from rest_framework import serializers

from .models import Post, Comment


class FilterCommentListSerializer(serializers.ListSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('content', )


class CommentSerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField()

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('id', 'post', 'comment', 'level', 'children')

    def get_children(self, obj):

        if obj.level < 2:
            return CommentSerializer(obj.children.all(), many=True).data
        else:
            return None


class AllCommentSerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField()

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('id', 'post', 'comment', 'level', 'children')

    def get_children(self, obj):
            return AllCommentSerializer(obj.children.all(), many=True).data
