from django.conf import settings
from django.db import models
from slugify import slugify
from apps.common.models import ActiveModel, TimeStampedModel


class Category(TimeStampedModel, ActiveModel):
    name = models.CharField(
        max_length=155, unique=True, verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=155, unique=True, blank=True, verbose_name="Slug"
    )

    class Meta:
        verbose_name="категория"
        verbose_name_plural="Категории"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Tag(TimeStampedModel, ActiveModel):
    name = models.CharField(
        max_length=155, unique=True, verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=155, unique=True, blank=True, verbose_name="Slug"
    )

    class Meta:
        verbose_name="тег"
        verbose_name_plural="Теги"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class PostStatus(models.TextChoices):
    DRAFT = 'draft', 'черновик'
    PUBLISHED = 'piblished', 'Опубликовано'
    ARCHIVED = 'archived', 'Архив'


class Post(TimeStampedModel, ActiveModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор'
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, 
        related_name='posts', verbose_name="Категория"
    )
    tags = models.ManyToManyField(
        Tag, related_name='posts', 
        blank=True, verbose_name='Теги'
    )
    title = models.CharField(
        max_length=155, verbose_name="Заголовок"
    )
    slug = models.SlugField(
        max_length=155, unique=True, 
        blank=True, verbose_name='Slug'
    )
    short_description = models.TextField(
        verbose_name="Краткое описание"
    )
    content = models.TextField(verbose_name="Содержимое")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров",
    )
    status = models.CharField(
        choices=PostStatus.choices, default=PostStatus.PUBLISHED,
        max_length=20, verbose_name="Статус",
    )

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title