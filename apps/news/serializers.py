from rest_framework import serializers
from apps.news.models import Category, Tag, Post 
from apps.comments.serializers import PostCommentSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'slug',
            'is_active', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'slug', 'created_at', 'updated_at'
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id', 'name', 'slug',
            'is_active', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'slug', 'created_at', 'updated_at'
        )


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True,read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = (
            "id", "title", "slug",
            "short_description", "content",
            "category", "tags", "author",
            "status", "views_count", "is_active",
            "created_at", "updated_at",
        )

class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True,read_only=True)
    author = serializers.StringRelatedField()
    comments = PostCommentSerializer(many=True,read_only=True)

    class Meta:
        model = Post
        fields = (
            "id", "title", "slug",
            "short_description", "content",
            "category", "tags", "author",
            "status", "views_count", "comments",  "is_active",
            "created_at", "updated_at",
        )


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id", "title", "slug",
            "short_description", "content",
            "category", "tags", "author",
            "status", "views_count", "is_active",
            "created_at", "updated_at",
        )
        read_only_fields = (
            'slug', "views_count", 
            'created_at', 'updated_at'
        )