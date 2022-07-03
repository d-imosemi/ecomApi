from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.contrib.auth import get_user_model


User = get_user_model()

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



# CATEGORY-------ENDPOINT-----------START

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticated)

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# CATEGORY-------ENDPOINT-----------END



# COLOR-------ENDPOINT-----------START

class ListColor(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class DetailColor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

# COLOR-------ENDPOINT-----------END



# SIZE-------ENDPOINT-----------START

class ListSize(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class DetailSize(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

# SIZE-------ENDPOINT-----------END


# PRODUCT-------ENDPOINT-----------START

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# PRODUCT-------ENDPOINT-----------END


# PRODUCT REVIEW-------ENDPOINT-----------START

class ListProductReview(generics.ListCreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class DetailProductReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PRODUCT REVIEW-------ENDPOINT-----------END



# CART-------ENDPOINT-----------START

class ListCart(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(cart_id=self.request.user)

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    # permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(cart_id=self.request.user)

class UpdateCartStatus(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartStatusSerializer
    # permission_classes = [IsAdmin]


class UserOrdersView(generics.GenericAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()
    # permission_classes = [IsAdmin]

    def get(self, request, user_pk):
        user = User.objects.get(pk=user_pk)

        carts = Cart.objects.all().filter(cart_id=user)

        serializer = self.serializer_class(instance=carts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrdersDetail(generics.GenericAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()
    # permission_classes = [IsAdmin]

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

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

# PROFILE-------ENDPOINT-----------END
