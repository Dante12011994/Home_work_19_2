from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        list = [
            {'category_name': 'еда', 'category_description': 'что-то'},
            {'category_name': 'одежда', 'category_description': 'что-нибудь'},
            {'category_name': 'техника', 'category_description': 'еще что-то'},
            {'category_name': 'транспорт', 'category_description': 'мда'},
        ]

        save = []
        for i in list:
            save.append(Category(**i))

        Category.objects.bulk_create(save)
