from django.contrib import admin

from .models import Category, Book, Color, Product


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Book)
admin.site.register(Product)


