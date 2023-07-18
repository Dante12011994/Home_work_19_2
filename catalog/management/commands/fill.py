from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        list = [
            {'id': 1, 'category_name': 'Еда', 'category_description': 'что-то'},
            {'id': 2, 'category_name': 'Одежда', 'category_description': 'что-нибудь'},
            {'id': 3, 'category_name': 'Техника', 'category_description': 'еще что-то'},
            {'id': 4, 'category_name': 'Транспорт', 'category_description': 'мда'},
        ]

        save = []
        for i in list:
            save.append(Category(**i))

        Category.objects.bulk_create(save)

