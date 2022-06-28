from rest_framework import serializers
from .models import BookReview, Cart, Category, Color, Product, Book, ProductReview, Size



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
        )



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'id',
            'name',
        )



class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'id',
            'name',
        )



class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    class Meta:
        model = Book
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


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    color = ColorSerializer(read_only=True, many=True)
    size = SizeSerializer(read_only=True, many=True)
    class Meta:
        model = Product
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
            'size',
            'description',
            'image',
            'status',
            'date_created',
        )

class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True, many=False)
    class Meta:
        model = BookReview
        fields = (
            'id',
            'user_id',
            'book',
            'review',
            'rating',
            'created_on',
        )

class ProductReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=False)
    class Meta:
        model = ProductReview
        fields = (
            'id',
            'user_id',
            'product',
            'review',
            'rating',
            'created_on',
        )

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    books = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'cart_id',
            'books',
            'products',
            'quantity',
            'created_on',
        )