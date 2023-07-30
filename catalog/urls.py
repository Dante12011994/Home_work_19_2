from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main, contact, ProductCreateView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),  # Страница "Главная"
    path('contact', contact, name='contact'),
    path('products', ProductListView.as_view(), name='products'),  # Страница "Контакты"
    path('create-product/', ProductCreateView.as_view(), name='create_product'),
]
