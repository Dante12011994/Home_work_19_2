from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    category_description = models.CharField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.CharField(max_length=1000, verbose_name='Описание')
    product_img = models.ImageField(upload_to='img/', verbose_name='Фотот товара', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    product_date_creation = models.DateTimeField(auto_now_add=True)
    product_last_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name}: {self.product_description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('product_name',)
