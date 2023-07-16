from django.shortcuts import render
import psycopg2
from catalog.models import Product


def main(request):
    """
    Переходит на страницу "Главная"
    """
    product_list = Product.objects.order_by('?')[:3]
    context = {'products': product_list}
    return render(request, 'catalog/main.html', context)


def contact(request):
    """
    Обрабатывает действия на странице "Контакты"
    """
    # Принимает информацию сообщения оставленого пользователем
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('massage')

        # Воводит сообщение в консоль
        print(f'{name} ({email}): {text}')
    return render(request, 'catalog/contact.html')
