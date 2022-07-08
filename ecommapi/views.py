from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework import filters
from django.contrib.auth import get_user_model
from .serializers import (
    CartDetailSerializer,
    CartStatusSerializer,
    CategorySerializer,
    ColorSerializer,
    CreateCartSerializer,
    ListProductSerializer,
    ProductReviewSerializer,
    ProductSerializer,
    ProfileSerializer,
    SizeSerializer,
    UpdateCartDetailSerializer
    )
from .models import Cart, Category, Color, Product, ProductReview, Profile, Size

User = get_user_model()


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Hello'}, status=status.HTTP_200_ok)

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



# COLOR-------ENDPOINT-----------START
# class ListColor(generics.ListAPIView):
#     queryset = Color.objects.all()
#     serializer_class = ColorSerializer
#     permission_classes = [permissions.AllowAny]


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

# class ListSize(generics.ListAPIView):
#     queryset = Size.objects.all()
#     serializer_class = SizeSerializer
#     permission_classes = [permissions.AllowAny]


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



# PRODUCT-------ENDPOINT-----------START

class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ListProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    ordering_fields  = ['created_on']

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


class CreateCart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(cart_id=self.request.user)

class ListCart(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    permission_classes = [permissions.IsAdminUser]

class DeleteDetailCart(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = UpdateCartDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(cart_id=self.request.user)

class UpdateDetailCart(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = UpdateCartDetailSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(cart_id=self.request.user)

class UpdateCartStatus(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartStatusSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [permissions.IsAdminUser]


class UserOrdersView(generics.GenericAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)

        carts = Cart.objects.all().filter(cart_id=user)

        serializer = self.serializer_class(instance=carts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrdersDetail(generics.GenericAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_pk, order_pk):
        user = User.objects.get(pk=user_pk)

        carts = Cart.objects.all().filter(cart_id=user).get(pk=order_pk)

        serializer = self.serializer_class(instance=carts)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
# CART-------ENDPOINT-----------END



class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PROFILE-------ENDPOINT-----------END
