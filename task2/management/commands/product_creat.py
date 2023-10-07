from random import random

from django.core.management import BaseCommand

import sys
sys.path.append("./Homework_2/hw_2/task2")

from task2.models import Product


class Command(BaseCommand):
    help = "Create fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Name_product_{i}',
                              description=f'product description {i}',
                              price=9999,
                              quantity=10
                              )
            product.save()
