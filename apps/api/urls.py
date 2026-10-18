from rest_framework.routers import DefaultRouter
from apps.news.viewsets import (
    CategoryViewSet, TagViewSet, PostViewSet
)
from apps.comments.viewsets import CommentViewSet

router = DefaultRouter()

router.register(
    'categories', CategoryViewSet, basename='categories'
)
router.register(
    'tags', TagViewSet, basename='tags'
)
router.register(
    'posts', PostViewSet, basename='posts'
)
router.register(
    'comments', CommentViewSet, basename='comments'
)

urlpatterns = router.urls
