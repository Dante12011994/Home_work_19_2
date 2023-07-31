# Generated by Django 4.2.3 on 2023-07-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Заголовок', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('body', models.TextField(verbose_name='Cодержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Превью статьи')),
                ('article_date_creation', models.DateTimeField(auto_now_add=True)),
                ('publication', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('views_count', models.ImageField(default=0, upload_to='', verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
