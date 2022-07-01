from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Cart, Category, Color, Product, ProductReview, Profile, Size



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created_on',
        )



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'id',
            'name',
            'created_on',
        )



class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'id',
            'name',
            'created_on',
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
            'author',
            'isbn',
            'pages',
            'description',
            'image1',
            'image2',
            'image3',
            'image4',
            'status',
            'updated_on',
            'created_on',
        )


class ProductReviewSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True, many=False)
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
    cart_id = UserSerializer(read_only=True, many=False)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'cart_id',
            'products',
            'total',
            'updated_on',
            'created_on',
        )


class ProfileSerializer(serializers.ModelSerializer):
    cart_id = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Profile
        fields = (
            'id',
            'cart_id',
            'address',
            'zipcode',
            'phonenumber',
            'country',
            'state',
            'gender',
            'updated_on',
            'created_on',
        )