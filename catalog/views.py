from django.forms import inlineformset_factory
from django.shortcuts import render
import psycopg2
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version


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
    """
    Выводит весь список товаров на страницу
    """
    model = Product


class ProductCreateView(CreateView):
    """
    Функционал для создания нового продукта, после возвращает на страницу со всеми товарами
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        """
        При создании товара, привязывает авторизированного пользователя к товару
        """
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductDetailView(DetailView):
    """
    Функционал для вывода информации о товаре
    """
    model = Product


class ProductUpdateView(UpdateView):
    """
    Функционал для изменения информации о товаре
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        """
        Реализует заполнение и сохранение версий товара
        """
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        """
        При изменение товара, привязывает авторизированного пользователя к товару
        """
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    """
    Функционал для удаления товара
    """
    model = Product
    success_url = reverse_lazy('catalog:products')
