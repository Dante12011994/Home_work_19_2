from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок', **NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Cодержимое', **NULLABLE)
    preview = models.ImageField(upload_to='media/', verbose_name='Превью статьи', **NULLABLE)
    article_date_creation = models.DateTimeField(auto_now_add=True)
    publication = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.ImageField(default=0, verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


