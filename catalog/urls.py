from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main, contact, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),  # Страница "Главная"
    path('contact', contact, name='contact'),
    path('products', ProductListView.as_view(), name='products'),
    path('create-product/', ProductCreateView.as_view(), name='create_product'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
