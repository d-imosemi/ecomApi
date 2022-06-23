from rest_framework import serializers
from .models import Category, Product, Book



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
        )
        model = Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'initial_price',
            'current_price',
            'stock',
            'description',
            'image',
            'status',
            'date_created',      
        )
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'tag',
            'name',
            'category',
            'initial_price',
            'current_price',
            'stock',
            'description',
            'image',
            'status',
            'date_created',
        )
        model = Product
