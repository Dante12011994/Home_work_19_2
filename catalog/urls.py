from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main, contact, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),  # Страница "Главная"
    path('contact', contact, name='contact'),  # Страница контатов
    path('products', ProductListView.as_view(), name='products'),  # Все товары
    path('create-product/', ProductCreateView.as_view(), name='create_product'),  # Создание товара
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),  # Информация о товаре
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),  # Изменение товара
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),  # Удаление товара
]
