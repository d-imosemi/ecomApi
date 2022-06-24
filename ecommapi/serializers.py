from rest_framework import serializers
from .models import Category, Color, Product, Book



class CategorySerializer(serializers.ModelSerializer):
    model = Category
    class Meta:
        fields = (
            'id',
            'title',
        )
    

class ColorSerializer(serializers.ModelSerializer):
    model = Color
    class Meta:
        fields = (
            'id',
            'name',
        )


class BookSerializer(serializers.ModelSerializer):
    model = Book
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
            'review',
            'date_created',      
        )
    

class ProductSerializer(serializers.ModelSerializer):
    model = Product
    class Meta:
        fields = (
            'id',
            'tag',
            'name',
            'category',
            'initial_price',
            'current_price',
            'stock',
            'sku',
            'color',
            'description',
            'image',
            'status',
            'review',
            'date_created',
        )
