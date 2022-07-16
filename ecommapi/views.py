from rest_framework.response import Response
from rest_framework import generics, status, permissions, exceptions
from rest_framework import filters
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.exceptions import NotAcceptable, ValidationError, PermissionDenied
from rest_framework.views import APIView

from django.utils.decorators import method_decorator
from .decorators import time_calculator


User = get_user_model()


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Welcome to the Ecommerce API'}, status=status.HTTP_204_NO_CONTENT)

# CATEGORY-------ENDPOINT-----------START
class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAdminUser]

# CATEGORY-------ENDPOINT-----------END


# SHIPPING-------ENDPOINT-----------START
class ListShipping(generics.ListAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    permission_classes = [permissions.AllowAny]

class CreateShipping(generics.CreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    permission_classes = [permissions.IsAdminUser]

class DetailShipping(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAdminUser]

# SHIPPING-------ENDPOINT-----------END



# COLOR-------ENDPOINT-----------START
class ListColor(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.AllowAny]


class CreateColor(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAdminUser]


class DetailColor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAdminUser]

# COLOR-------ENDPOINT-----------END



# SIZE-------ENDPOINT-----------START

class ListSize(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [permissions.AllowAny]


class CreateSize(generics.CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [permissions.IsAdminUser]


class DetailSize(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAdminUser]

# SIZE-------ENDPOINT-----------END



# ADDRESS-------ENDPOINT-----------END


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ['get', 'put',]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        address = self.get_object()
        if address.user_id != user:
            raise NotAcceptable("this addrss don't belong to you")
        serializer = self.get_serializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)



# ADDRESS-------ENDPOINT-----------END




# PRODUCT-------ENDPOINT-----------START

class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ListProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAdminUser]

# PRODUCT-------ENDPOINT-----------END



# PRODUCT REVIEW-------ENDPOINT-----------START

class CreateProductReview(generics.CreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class ListProductReview(generics.ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.AllowAny]


class DetailProductReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PRODUCT REVIEW-------ENDPOINT-----------END




# PROFILE-------ENDPOINT-----------STATRT


class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put',]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PROFILE-------ENDPOINT-----------END


class UpdateCartStatus(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartStatusSerializer
    http_method_names = ['put']
    permission_classes = [permissions.IsAdminUser]



# CARTITEM-------ENDPOINT-----------START


class CartItemAPIView(ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CartItem.objects.filter(cart__user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        product = get_object_or_404(Product, pk=request.data["product"])
        current_item = CartItem.objects.filter(cart=cart, product=product)

        if user == product.user:
            raise PermissionDenied("This Is Your Product")

        if current_item.count() > 0:
            raise NotAcceptable("You already have this item in your shopping cart")

        try:
            quantity = int(request.data["quantity"])
        except Exception as e:
            raise ValidationError("Please Enter Your Quantity")

        if quantity > product.stock:
            raise NotAcceptable("You order quantity is more than the seller have")

        cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        total = float(product.current_price) * float(quantity)
        cart.total = total
        cart.save()
        # push_notifications(
        #     cart.user,
        #     "New cart product",
        #     "you added a product to your cart " + product.name,
        # )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    http_method_names = ['get', 'put', 'delete',]
    queryset = CartItem.objects.all()

    def retrieve(self, request, *args, **kwargs):
        cart_item = self.get_object()
        if cart_item.cart.user != request.user:
            raise PermissionDenied("Sorry this cart does not belong to you")
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cart_item = self.get_object()
        print(request.data)
        product = get_object_or_404(Product, pk=request.data["product"])

        if cart_item.cart.user != request.user:
            raise PermissionDenied("Sorry this cart does not belong to you")

        try:
            quantity = int(request.data["quantity"])
        except Exception as e:
            raise ValidationError("Please, input a vaild quantity")

        if quantity > product.stock:
            raise NotAcceptable("Your order quantity is more than the seller Quantity")

        serializer = CartItemUpdateSerializer(cart_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        cart_item = self.get_object()
        if cart_item.cart.user != request.user:
            raise PermissionDenied("Sorry this cart does not belong to you")
        cart_item.delete()
        # push_notifications(
        #     cart_item.cart.user,
        #     "deleted cart product",
        #     "you have deleted this product: "
        #     + cart_item.product.name
        #     + " from your cart",
        # )

        return Response(
            {"detail": ("your item has been deleted.")},
            status=status.HTTP_204_NO_CONTENT,
        )

# CARTITEM-------ENDPOINT-----------END



# ORDER-------ENDPOINT-----------END


class OrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @time_calculator
    def time(self):
        return 0

    def post(self, request, pk, *args, **kwargs):
        user = request.user
        user_address = Address.objects.filter(user_id=user).first()
        product = get_object_or_404(Product, pk=pk)
        if product.stock == 0:
            raise exceptions.NotAcceptable("No Product available")
        try:
            order_number = request.data.get("order_number", 1)
            quantity = request.data.get("quantity", 1)
        except:
            pass

        total = quantity * product.current_price
        order = Order().create_order(user, order_number, user_address, True)
        order_item = OrderItem().create_order_item(order, product, quantity, total)
        serializer = OrderItemMiniSerializer(order_item)
        # push_notifications(
        #     user,
        #     "Request Order",
        #     "your order: #" + str(order_number) + " has been sent successfully.",
        # )
        self.time()
        # TODO Payment Integration here.
        # TODO send Email to seller and buyer
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def Payment(request):
    return render(request, "payment/payment.html", {})


# ORDER-------ENDPOINT-----------END





# CHECKOUT-------ENDPOINT-----------START

class CheckoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        # address_id = request.data.get("address")
        user_address = Address.objects.filter(user_id=user).first()
        # user_address = Address.objects.filter(id=address_id, user_id=user)[0]
        product = get_object_or_404(Product, pk=pk)
        
        cart = get_object_or_404(Cart, user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            ecommerce_fees = item.shipping
        total = ecommerce_fees + (product.current_price * item.quantity)
        data = {}
        data["address"] = AddressSerializer(user_address).data
        data["product"] = ProductCreateCartSerializer(
            product, context={"request": request}
        ).data
        data["Shipping Fee"] = ecommerce_fees
        data["total"] = total

        return Response(data, status=status.HTTP_200_OK)


class CheckoutCartView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        # address_id = request.data.get("address")
        data = {}
        total = 0
        quantity = 0
        user_address = Address.objects.filter(user_id=user).first()
        # user_address = Address.objects.filter(id=address_id, user_id=user)[0]
        cart = get_object_or_404(Cart, user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            total += item.total
            quantity += item.quantity
            ecommerce_fees = item.shipping
            extra_shipping = 1000
            if quantity >= 10:
                end_total =  ecommerce_fees + (total + extra_shipping)
            else:
                end_total =  ecommerce_fees + (total)


        data["address"] = AddressSerializer(user_address).data
        data["items"] = CartItemMiniSerializer(cart_items, many=True).data
        data["Shipping fee"] = ecommerce_fees
        if quantity >= 10:
            data["extra Shipping fee"] = extra_shipping
        data["total"] = end_total
        return Response(data, status=status.HTTP_200_OK)

# CHECKOUT-------ENDPOINT-----------END




