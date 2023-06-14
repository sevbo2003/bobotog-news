from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class Category(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, verbose_name=_('Kategoriya nomi'))
    image = models.ImageField(upload_to='category_images', verbose_name=_('Rasm'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Kategoriya')
        verbose_name_plural = _('Kategoriyalar')


class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=300, verbose_name=_('Sarlavha'))
    content = CKEditor5Field(config_name='extends', verbose_name=_('Maqola'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Kategoriya'))
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)
    dolzarb = models.BooleanField(default=False, verbose_name=_('Dolzarb'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Maxus post'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'))
    views = models.IntegerField(default=0, verbose_name=_('Ko\'rilganlar soni'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Maqola')
        verbose_name_plural = _('Maqolalar')
        ordering = ['-created_at']


class PostImage(models.Model):
    image = models.ImageField(upload_to='post_images', verbose_name=_('Rasm'), null=True, blank=True)
    video = models.FileField(upload_to='post_videos', verbose_name=_('Video'), null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Maqola'))

    def __str__(self):
        return self.post.title
    
    class Meta:
        verbose_name = _('Maqola rasm')
        verbose_name_plural = _('Maqola rasmlari')

