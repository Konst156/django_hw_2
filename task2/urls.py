from django.urls import path

from . import views

# from homework_django.hw_1.hw_1 import views


urlpatterns = [
    path('', views.main, name='Главная'),
    path('about/', views.about, name='Обо мне'),
    path('clients/', views.get_all_clients, name='Клиенты'),
    path('products/', views.get_all_products, name='Продукты'),
    path('orders/', views.get_all_orders, name='Заказы'),
]