from django.db import models
from apps.common.models import ActiveModel, TimeStampedModel
from apps.news.models import Post


class Comment(TimeStampedModel, ActiveModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments', verbose_name="Публикация"
    )
    author_name = models.CharField(
        max_length=100, verbose_name="Имя автора"
    )
    text = models.TextField(verbose_name='Комментарии')

    def __str__(self):
        return f"{self.author_name}: {self.post.title}"
    
    class Meta:
        verbose_name="комментарии"
        verbose_name_plural="Комментарии"
        ordering = ('-created_at',)