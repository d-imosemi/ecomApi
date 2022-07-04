from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly 
from rest_framework import filters
from django.contrib.auth import get_user_model
from .serializers import (
    CartDetailSerializer,
    CartStatusSerializer,
    CategorySerializer,
    ColorSerializer,
    CreateCartSerializer,
    ProductReviewSerializer,
    ProductSerializer,
    ProfileSerializer,
    SizeSerializer
    )
from .models import Cart, Category, Color, Product, ProductReview, Profile, Size

User = get_user_model()



# CATEGORY-------ENDPOINT-----------START
class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny)

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser)

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser)

# CATEGORY-------ENDPOINT-----------END



# COLOR-------ENDPOINT-----------START
class ListColor(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (AllowAny)


class CreateColor(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser)


class DetailColor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser)

# COLOR-------ENDPOINT-----------END



# SIZE-------ENDPOINT-----------START

class ListSize(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (AllowAny)

class CreateSize(generics.CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (IsAdminUser)


class DetailSize(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (IsAdminUser)

# SIZE-------ENDPOINT-----------END



# PRODUCT-------ENDPOINT-----------START

class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    ordering_fields  = ['created_on']
    # permission_classes = (AllowAny)

class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser)

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser)

# PRODUCT-------ENDPOINT-----------END


# PRODUCT REVIEW-------ENDPOINT-----------START

class CreateProductReview(generics.CreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class ListProductReview(generics.ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class DetailProductReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PRODUCT REVIEW-------ENDPOINT-----------END



# CART-------ENDPOINT-----------START

class CreateCart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(cart_id=self.request.user)

class ListCart(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(cart_id=self.request.user)

class UpdateCartStatus(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartStatusSerializer
    permission_classes = [IsAdminUser]


class UserOrdersView(generics.GenericAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)

        carts = Cart.objects.all().filter(cart_id=user)

        serializer = self.serializer_class(instance=carts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrdersDetail(generics.GenericAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, user_pk, order_pk):
        user = User.objects.get(pk=user_pk)

        carts = Cart.objects.all().filter(cart_id=user).get(pk=order_pk)

        serializer = self.serializer_class(instance=carts)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
# CART-------ENDPOINT-----------END




# PROFILE-------ENDPOINT-----------START

class ListProfile(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PROFILE-------ENDPOINT-----------END
