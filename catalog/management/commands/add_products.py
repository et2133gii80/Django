from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавьте продукты в базу данных'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(category_name = 'LG', description = 'Все продукты компании LG')

        products = [
            {'product_name':'Телевизор от LG',
             'description':'Хорошее качество экрана и изображения',
             'img':'',
             'category':'LG',
             'price': 4444,
             'created_at': '2025-09-12',
             'updated_at': '2025-10-12',
             'group': category,
             },

            {'product_name':'Монитор от LG',
             'description':'Хорошее качество изображения',
             'img':'',
             'category':'LG',
             'price': 11111,
             'created_at': '2025-09-13',
             'updated_at': '2025-10-13',
             'group': category,}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Успешное добавление продукта: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже существует: {product.product_name}'))
