from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        list_ = [
            {'product_name': 'Картошка', 'product_description': 'Очень вкусная, если пожарить на сковородочке с лучком',
             'product_img': 'картошка.jpg', 'category': Category.objects.get(pk=1), 'product_price': '25'},
            {'product_name': 'Колбаса', 'product_description': 'Положи на хлеб, а потов съешь',
             'product_img': 'колбаса.jpg', 'category': Category.objects.get(pk=1), 'product_price': '180'},
            {'product_name': 'Хлеб', 'product_description': 'Тот самый, на который кладут колбасу',
             'product_img': 'хлеб.jpg', 'category': Category.objects.get(pk=1), 'product_price': '46'},
            {'product_name': 'Кросовки', 'product_description': 'Очень удобно бегать',
             'product_img': 'кросовки.jpg', 'category': Category.objects.get(pk=2), 'product_price': '18962'},
            {'product_name': 'Пальто', 'product_description': 'Чтобы выглядеть сольдно и не мерзнуть',
             'product_img': 'пальто.jpg', 'category': Category.objects.get(pk=2), 'product_price': '25000'},
            {'product_name': 'Футболка', 'product_description': 'Смешная и удобная',
             'product_img': 'футболка.jpg', 'category': Category.objects.get(pk=2), 'product_price': '350'},
            {'product_name': 'Телефон', 'product_description': 'Без него сейчас невозможно обойтись',
             'product_img': 'телефон.jpg', 'category': Category.objects.get(pk=3), 'product_price': '27000'},
            {'product_name': 'Телевизор', 'product_description': 'Самая бесполезная вешь в доме, но без нее трудно представить существование',
             'product_img': 'телевизор.jpg', 'category': Category.objects.get(pk=3), 'product_price': '7600'},
            {'product_name': 'Масляный радиатор', 'product_description': 'Как же приятно прижаться к нему зимой',
             'product_img': 'радиатор.jpg', 'category': Category.objects.get(pk=3), 'product_price': '6350'}
        ]

        save_list = []

        for i in list_:
            save_list.append(Product(**i))

        Product.objects.bulk_create(save_list)