from rest_framework import serializers

from .models import Post, Comment


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)

        return serializer.data


class FilterCommentListSerializer(serializers.ListSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('content', )


class CommentSerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField()



    def get_children(self, obj):

        return RecursiveSerializer(obj) if obj.level <= 3 else None
        # if obj.level <= 3:
        #     return children
        # else:
        #     None

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('post', 'comment', 'level', 'children')



