from django.urls import path

from catalog.views import main, contact, products

urlpatterns = [
    path('', main, name='main'),  # Страница "Главная"
    path('contact', contact, name='contact'),
    path('products', products, name='products')  # Страница "Контакты"
]
