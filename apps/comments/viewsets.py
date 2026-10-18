from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.select_related('post')
    serializer_class = CommentSerializer

    filter_backends = (
        DjangoFilterBackend, OrderingFilter
    )
    filterset_fields = ('post', 'is_active')
    ordering_fields = ('created_at',)
    ordering = ('-created_at',)
