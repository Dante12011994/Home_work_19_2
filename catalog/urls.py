from django.urls import path

from catalog.views import main, contact

urlpatterns = [
    path('', main, name='main'),  # Страница "Главная"
    path('contact', contact, name='contact'),  # Страница "Контакты"
]
