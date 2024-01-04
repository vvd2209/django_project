from django.db import models

from catalog.constants import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    data_create = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    is_publish = models.BooleanField(default=True, verbose_name='Признак публикации')
    count_view = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
