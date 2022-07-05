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

class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
        )


class ListColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'name',
        )


class ListSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'name',
        )


class ProductSerializer(serializers.ModelSerializer):
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

class ListProductSerializer(serializers.ModelSerializer):
    color = ListColorSerializer(many=True, read_only=True)
    size = ListSizeSerializer(many=True, read_only=True)
    category = ListCategorySerializer(many=False, read_only=True)
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
    user_id = serializers.SerializerMethodField()
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

        read_only_fields = ['user_id']
    def get_user_id(self, obj):
        return obj.user_id.username



# class ProductCreateCartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = (
#             'name',
#         )


class CreateCartSerializer(serializers.ModelSerializer):
    cart_id = serializers.SerializerMethodField()
    status = serializers.HiddenField(default='PENDING')
    # order_item = ProductCreateCartSerializer(read_only=False, many=False)
    # color = ListColorSerializer(many=True, read_only=True)
    # size = ListSizeSerializer(many=True, read_only=False)
    class Meta:
        model = Cart
        fields = (
            'cart_id',
            'order_item',
            'color',
            'size',
            'status',
            'quantity',
        )

        read_only_fields = ['cart_id']

    def get_cart_id(self, obj):
        return obj.cart_id.username

class CartDetailSerializer(serializers.ModelSerializer):
    cart_id = serializers.SerializerMethodField()
    status = serializers.CharField(default='PENDING')
    updated_on = serializers.DateTimeField()
    created_on = serializers.DateTimeField()
    # products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = (
            'id',
            'cart_id',
            'order_item',
            'status',
            'quantity',
            'updated_on',
            'created_on',
        )

        read_only_fields = ['cart_id']

    def get_cart_id(self, obj):
        return obj.cart_id.username

class UpdateCartDetailSerializer(serializers.ModelSerializer):
    cart_id = serializers.SerializerMethodField()
    # products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = (
            'id',
            'cart_id',
            'order_item',
            'quantity',
        )

        read_only_fields = ['cart_id']

    def get_cart_id(self, obj):
        return obj.cart_id.username



class CartStatusSerializer(serializers.ModelSerializer):
     class Meta:
        model = Cart
        fields = (
            'status',
        )



class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = (
            'id',
            'user_id',
            'address',
            'zipcode',
            'country',
            'state',
            'gender',
            'updated_on',
            'created_on',
        )
        read_only_fields = ['user_id']

    def get_user_id(self, obj):
        return obj.user_id.username
