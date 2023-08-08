from django.conf import settings
from django.db import models

# Параметры для необязательных полей модели
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    Модель "Категория товаров"
    """
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    category_description = models.CharField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    """
    Модель "Товар", привязывается к категории
    """
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.CharField(max_length=1000, verbose_name='Описание')
    product_img = models.ImageField(upload_to='img/', verbose_name='Фотот товара', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    product_date_creation = models.DateTimeField(auto_now_add=True)
    product_last_change = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Продавец', **NULLABLE)

    def __str__(self):
        return f'{self.product_name}: {self.product_description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('product_name',)


class Version(models.Model):
    """
    Модель "Версия", привязывается к товару
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='version')
    number_vers = models.PositiveIntegerField(default=0, verbose_name='Номер версии')
    name = models.CharField(max_length=250, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Активная версия')

    def __str__(self):
        return f'{self.name}, {self.product}, {self.number_vers}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

