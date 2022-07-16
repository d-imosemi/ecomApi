from accounts.serializers import MainUserSerializer
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'created_on',
        ]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'name',
            'created_on',
        ]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = [
            'name',
            'created_on',
        ]

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = [
            'name',
            'price',
            'created_on',
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ["updated_on", 'user_id',]


class CreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ["user_id",]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'tag',
            'name',
            'category',
            'initial_price',
            'discount_percent',
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
        ]

class ListProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = [
            'tag',
            'name',
            'category',
            'discount_percent',
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
            'created_on',
            'updated_on',
        ]


class ProductReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    class Meta:
        model = ProductReview
        fields = [
            'user_id',
            'product',
            'review',
            'rating',
            'created_on',
        ]

        read_only_fields = ['user_id']
    def get_user_id(self, obj):
        return obj.user_id.username



class ProductCreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'current_price',
        ]


class CheckoutSerializer(serializers.ModelSerializer):
    shipping = ShippingSerializer(read_only = True)
    class Meta:
        model = Cart
        fields = [
            'shipping_location',
            'grand_total',
        ]
    


class CartStatusSerializer(serializers.ModelSerializer):
     class Meta:
        model = Order
        fields = [
            'status',
            'is_paid',
            'updated_on',
        ]



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'discount_percent',
            'current_price',
            'image1',
        ]

class CartItemSerializer(serializers.ModelSerializer):
    product = CartProductSerializer(required = False, read_only=True)
    class Meta:
        model = CartItem
        fields = [
            'cart',
            'product',
            'quantity',
            'color',
            'size',
        ]

class CartItemMiniSerializer(serializers.ModelSerializer):
    product = CartProductSerializer(required = False, read_only=True)
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'color', 'size',]

class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'color', 'size',]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'gender',
            'created_on',
            'updated_on',
        ]
       




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["updated_on",]


class OrderMiniSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    user = MainUserSerializer(required=False)

    class Meta:
        model = Order
        exclude = ["updated_on",]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ["updated_on",]


class OrderItemMiniSerializer(serializers.ModelSerializer):
    order = OrderMiniSerializer(required=False, read_only=True)
    product = CartProductSerializer(required=False, read_only=True)

    class Meta:
        model = OrderItem
        exclude = ["updated_on",]







