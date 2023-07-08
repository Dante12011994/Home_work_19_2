
from django.urls import path

from catalog.views import main, contact

urlpatterns = [
    path('', contact),
    path('', main),

]
