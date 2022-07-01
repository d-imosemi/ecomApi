from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name = 'singlecategory'),

    path('colors/', ListColor.as_view(), name='colors'),
    path('colors/<int:pk>/', DetailColor.as_view(), name = 'singlecolor'),


    path('sizes/', ListSize.as_view(), name='sizes'),
    path('sizes/<int:pk>/', DetailSize.as_view(), name = 'singlesize'),


    path('products/', ListProduct.as_view(), name='products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='singleproduct'),


    path('productreviews/', ListProductReview.as_view(), name='productreviews'),
    path('productreviews/<int:pk>', DetailProductReview.as_view(), name='singleproductreview'),


    path('carts/', ListCart.as_view(), name='carts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='singlecarts'),


    path('profiles/', ListProfile.as_view(), name='profiles'),
    path('profiles/<int:pk>', DetailProfile.as_view(), name='singleprofile'),
]
