from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apps.comments.models import Comment
from apps.news.models import Category, Tag, Post 
from apps.news.serializers import (
    CategorySerializer, TagSerializer, 
    PostListSerializer, PostDetailSerializer, PostWriteSerializer 
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(ModelViewSet):
    filter_backends = (
        DjangoFilterBackend, SearchFilter, OrderingFilter
    )
    filterset_fields = (
        'category', 'status', 'is_active', 'author'
    )
    search_fields = (
        'title', 'short_description', 'content'
    )
    ordering_fields = (
        'created_at', 'updated_at', 'views_count', 'title'
    )
    ordering = ('created_at',)
    
    def get_queryset(self):
        queryset = (
            Post.objects.select_related('author', 'category')
            .prefetch_related('tags')
        )
        if self.action == 'retrieve':
            queryset = queryset.prefetch_related(
                Prefetch(
                    'comments', queryset=Comment.objects.filter(
                        is_active=True,
                    ).order_by('-created_at')
                )
            )
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostWriteSerializer
    
    
    
    
    

