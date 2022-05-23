from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),  # http://127.0.0.1:8000
    path('item/<int:id>', views.item_page), # http://127.0.0.1:8000/item/1 http://127.0.0.1:8000/item/2
    path('items', views.items_list), # http://127.0.0.1:8000/item/1 http://127.0.0.1:8000/item/2
]

# 1. Функции-обработчики
# 2. CBV
# ....
