from django.http import HttpResponse
import logging
from .models import Order, Product, Client

logger = logging.getLogger(__name__)


def main(request):
    html = """
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Здесь вы найдете много интересного!</p>
    """
    logger.info('Посещена главная страница')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Я - разработчик Django.</p>
    """
    logger.info('Посещена страница "О себе"')
    return HttpResponse(html)


def create_client(name, email, phone_number, address):
    client = Client(name=name, email=email, phone_number=phone_number, address=address)
    client.save()
    return client


# Получение всех клиентов
def get_all_clients(request):
    clients = Client.objects.all()
    return HttpResponse(clients)


# Получение клиента по его ID
def get_client_by_id(client_id):
    return Client.objects.get(pk=client_id)


# Обновление информации о клиенте
def update_client(client, name, email, phone_number, address):
    client.name = name
    client.email = email
    client.phone_number = phone_number
    client.address = address
    client.save()


# Удаление клиента
def delete_client(client):
    client.delete()


# Создание нового товара
def create_product(name, description, price, quantity):
    product = Product(name=name, description=description, price=price, quantity=quantity)
    product.save()
    return product


# Получение всех товаров
def get_all_products(request):
    products = Product.objects.all()
    return HttpResponse(products)


# Получение товара по его ID
def get_product_by_id(product_id):
    return Product.objects.get(pk=product_id)


# Обновление информации о товаре
def update_product(product, name, description, price, quantity):
    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity
    product.save()


# Удаление товара
def delete_product(product):
    product.delete()


# Создание нового заказа
def create_order(client, products, total_amount):
    order = Order(client=client, total_amount=total_amount)
    order.save()
    order.products.set(products)
    return order


# Получение всех заказов
def get_all_orders(request):
    orders = Order.objects.all()
    return HttpResponse(orders)


# Получение заказа по его ID
def get_order_by_id(order_id):
    return Order.objects.get(pk=order_id)


# Обновление информации о заказе
def update_order(order, client, products, total_amount):
    order.client = client
    order.total_amount = total_amount
    order.save()
    order.products.set(products)


# Удаление заказа
def delete_order(order):
    order.delete()
