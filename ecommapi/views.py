from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework import filters
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *



from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.exceptions import NotAcceptable, ValidationError, PermissionDenied
from rest_framework.views import APIView


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

# class ListAddressAPIView(ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = AddressSerializer

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Address.objects.filter(user=user)
#         return queryset


class AddressDetailView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        address = self.get_object()
        if address.user_id != user:
            raise NotAcceptable("this addrss don't belong to you")
        serializer = self.get_serializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)


class createAddressAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateAddressSerializer
    queryset = ""

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, primary=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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

# class ListProductReview(generics.ListAPIView):
#     queryset = ProductReview.objects.all()
#     serializer_class = ProductReviewSerializer
#     permission_classes = [permissions.AllowAny]


class DetailProductReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PRODUCT REVIEW-------ENDPOINT-----------END



# CART-------ENDPOINT-----------START


# class CreateCart(generics.CreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CreateUpdateCartDetailSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(cart_id=self.request.user)

# class ListCart(generics.ListAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartDetailSerializer
#     # permission_classes = [permissions.IsAdminUser]

# class DeleteDetailCart(generics.DestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartDetailSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def perform_update(self, serializer):
#         serializer.save(cart_id=self.request.user)

# class UpdateDetailCart(generics.UpdateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CreateUpdateCartDetailSerializer
#     http_method_names = ['get', 'post', 'put']
#     # permission_classes = [permissions.IsAuthenticated]

#     def perform_update(self, serializer):
#         serializer.save(cart_id=self.request.user)

# class UpdateCartStatus(generics.UpdateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartStatusSerializer
#     http_method_names = ['get', 'put']
#     permission_classes = [permissions.IsAdminUser]


# class UserOrdersView(generics.GenericAPIView):
#     serializer_class = CartDetailSerializer
#     queryset = Cart.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, user_pk):
#         user = User.objects.get(pk=user_pk)

#         carts = Cart.objects.all().filter(cart_id=user)

#         serializer = self.serializer_class(instance=carts, many=True)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# class UserOrdersDetail(generics.GenericAPIView):
#     serializer_class = CartDetailSerializer
#     queryset = Cart.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, user_pk, order_pk):
#         user = User.objects.get(pk=user_pk)

#         carts = Cart.objects.all().filter(cart_id=user).get(pk=order_pk)

#         serializer = self.serializer_class(instance=carts)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)
# CART-------ENDPOINT-----------END



# PROFILE-------ENDPOINT-----------STATRT


class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PROFILE-------ENDPOINT-----------END






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

        if quantity > product.quantity:
            raise NotAcceptable("You order quantity more than the seller have")

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




# CHECKOUT-------ENDPOINT-----------START

class CheckoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        address_id = request.data.get("address")
        # user_address = Address.objects.filter(id=address_id, user_id=user)[0]
        product = get_object_or_404(Product, pk=pk)
        
        cart = get_object_or_404(Cart, user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            ecommerce_fees = item.shipping
        total = ecommerce_fees + (product.current_price * item.quantity)
        data = {}
        # data["address"] = AddressSerializer(user_address).data
        data["product"] = ProductCreateCartSerializer(
            product, context={"request": request}
        ).data
        data["Shipping fee"] = ecommerce_fees
        data["total"] = total

        return Response(data, status=status.HTTP_200_OK)


class CheckoutCartView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        address_id = request.data.get("address")
        data = {}
        total = 0
        quantity = 0
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


        # data["address"] = AddressSerializer(user_address).data
        data["items"] = CartItemMiniSerializer(cart_items, many=True).data
        data["Shipping fee"] = ecommerce_fees
        if quantity >= 10:
            data["extra Shipping fee"] = extra_shipping
        data["total"] = end_total
        return Response(data, status=status.HTTP_200_OK)

# CHECKOUT-------ENDPOINT-----------END
