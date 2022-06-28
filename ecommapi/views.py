from rest_framework import generics
from .serializers import (
    BookReviewSerializer,
    CartSerializer,
    CategorySerializer,
    ColorSerializer,
    ProductReviewSerializer,
    ProductSerializer,
    BookSerializer,
    SizeSerializer
    )
from .models import BookReview, Cart, Category, Book, Color, Product, ProductReview, Size



class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ListColor(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class DetailColor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer



class ListSize(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class DetailSize(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer



class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ListBookReview(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer

class DetailBookReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer



class ListProductReview(generics.ListCreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

class DetailProductReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer



class ListCart(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer