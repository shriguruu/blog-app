from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help = 'This command populates the database with category data'

    def handle(self, *args:Any, **options:Any):
        Category.objects.all().delete()  # Clear existing data
        category = ['Smart Phones', 'Laptops', 'PC', 'Gaming', 'Travel', 'Food']
           

        for category_name in category:
            Category.objects.create(name = category_name)
        
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))