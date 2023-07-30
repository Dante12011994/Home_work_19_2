from django.shortcuts import render
import psycopg2
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from catalog.models import Product, Category


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


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_img', 'category', 'product_price')
    success_url = reverse_lazy('catalog:products')
