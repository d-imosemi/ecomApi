from django.urls import path
from .views import *

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name = 'singlecategory'),

    path('colors', ListColor.as_view(), name='colors'),
    path('colors/<int:pk>/', DetailColor.as_view(), name = 'singlecolor'),

    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),

    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='singleproduct'),
]
