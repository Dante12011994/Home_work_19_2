
from django.urls import path

from catalog.views import main, contact

urlpatterns = [
    path('', main), # Первая страница
    path('main', main), # Страница "Главная"
    path('contact', contact), # Страница "Контакты"
]
