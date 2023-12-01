from django.db import models
from django.urls import reverse

# Create your models here.

NULLABLE = {'blank': True, 'null': True} # **NULLABLE - необязательное поле для заполнения

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)

    # def get_absolute_url(self):
    #     return reverse('catalog:products', kwargs={'pk':self.pk})

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')
    picture = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE) # **NULLABLE - необязательное поле для заполнения
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_last_modified = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)

class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='контакты')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name',)