from django.core.management.base import BaseCommand
from shop.models import Category, Product

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        categories = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Home & Kitchen', 'slug': 'home-kitchen'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Toys & Games', 'slug': 'toys-games'},
        ]

        for cat in categories:
            Category.objects.create(**cat)

        products = [
            {'name': 'iPhone 13', 'slug': 'iphone-13', 'description': 'Latest model with A15 Bionic chip, 5G capability, and improved camera system.', 'price': 999.99, 'stock': 50, 'category': Category.objects.get(slug='electronics')},
            {'name': 'MacBook Air', 'slug': 'macbook-air', 'description': 'Lightweight and powerful laptop with M1 chip and 13-inch Retina display.', 'price': 1249.99, 'stock': 30, 'category': Category.objects.get(slug='electronics')},
            {'name': 'Classic White T-Shirt', 'slug': 'classic-white-t-shirt', 'description': '100% cotton, comfortable and stylish.', 'price': 19.99, 'stock': 100, 'category': Category.objects.get(slug='clothing')},
            {'name': 'Skinny Fit Jeans', 'slug': 'skinny-fit-jeans', 'description': 'High-quality denim with a skinny fit.', 'price': 49.99, 'stock': 70, 'category': Category.objects.get(slug='clothing')},
            {'name': 'Ninja Blender', 'slug': 'ninja-blender', 'description': 'High-powered blender perfect for smoothies and sauces.', 'price': 89.99, 'stock': 40, 'category': Category.objects.get(slug='home-kitchen')},
            {'name': 'Stainless Steel Cookware Set', 'slug': 'stainless-steel-cookware-set', 'description': 'Durable and versatile cookware set, includes pots and pans.', 'price': 199.99, 'stock': 20, 'category': Category.objects.get(slug='home-kitchen')},
            {'name': 'The Great Gatsby', 'slug': 'the-great-gatsby', 'description': 'A classic novel by F. Scott Fitzgerald.', 'price': 14.99, 'stock': 200, 'category': Category.objects.get(slug='books')},
            {'name': 'Atomic Habits', 'slug': 'atomic-habits', 'description': 'An Easy & Proven Way to Build Good Habits & Break Bad Ones by James Clear.', 'price': 16.99, 'stock': 150, 'category': Category.objects.get(slug='books')},
            {'name': 'Marvel Spider-Man Action Figure', 'slug': 'spiderman-action-figure', 'description': '6-inch action figure with multiple points of articulation.', 'price': 24.99, 'stock': 80, 'category': Category.objects.get(slug='toys-games')},
            {'name': 'Catan', 'slug': 'catan-board-game', 'description': 'Popular strategy board game for 3-4 players.', 'price': 44.99, 'stock': 60, 'category': Category.objects.get(slug='toys-games')},
        ]

        for prod in products:
            Product.objects.create(**prod)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
