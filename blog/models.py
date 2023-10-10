from django.db import models

from service.models import NULLABLE


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    content = models.TextField(**NULLABLE, verbose_name='содержание')
    preview = models.ImageField(upload_to='article/', **NULLABLE, verbose_name='изображение')
    quantity = models.IntegerField(default=0, verbose_name='количество просмотров')
    created_at = models.DateField(auto_now_add=True, **NULLABLE, verbose_name='дата создания')
    sign = models.BooleanField(default=True, verbose_name='признак публикации')

    def __str__(self):
        return f'{self.title} ({self.quantity} просмотров)'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
