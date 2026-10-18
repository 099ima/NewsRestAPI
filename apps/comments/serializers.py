from rest_framework.serializers import ModelSerializer
from apps.comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id', 'post', 'text', 'author_name',
            'is_active', 'created_at', 'updated_at', 
        )
        read_only_fields = (
            'created_at', 'updated_at', 
        )


class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "author_name",
            "created_at",
        )
        read_only_fields = (
            "id",
            "created_at",
        )