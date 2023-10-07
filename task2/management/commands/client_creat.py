from random import random, choice

from django.core.management import BaseCommand

import sys

sys.path.append("./Homework_2/hw_2/task2")

from task2.models import Product, Client, Order


class Command(BaseCommand):
    help = "Create fake clients, orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count clients')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        # all_products = list(Product.objects.all())
        for i in range(1, count + 1):
            client = Client(name=f'Name_{i}',
                            email=f'mail_{i}@mail.ru',
                            phone_number=12345678910,
                            address=f'Адрес_{i}')
            client.save()
            for j in range(1, count + 1):
                order = Order(
                    client=client,
                    # products=choice(all_products),
                    total_amount= 777777
                )
                order.save()
