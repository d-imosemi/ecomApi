from django.urls import path
from .views import *

urlpatterns = [
    path('', HelloAuthView.as_view(), name='home'),
    path('list_categories/', ListCategory.as_view(), name='list_categories'),
    path('Create_category/', CreateCategory.as_view(), name='create_categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name = 'single_category'),

    path('list_colors/', ListColor.as_view(), name='list_colors'),
    path('create_color/', CreateColor.as_view(), name='create_colors'),
    path('colors/<int:pk>/', DetailColor.as_view(), name = 'singlecolor'),


    path('list_sizes/', ListSize.as_view(), name='list_sizes'),
    path('create_size/', CreateSize.as_view(), name='Create_sizes'),
    path('sizes/<int:pk>/', DetailSize.as_view(), name = 'singlesize'),


    path('list_products/', ListProduct.as_view(), name='list_products'),
    path('create_products/', CreateProduct.as_view(), name='create_products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='singleproduct'),


    path('productreviews/', CreateProductReview.as_view(), name='productreviews'),
    path('list_productreviews/', ListProductReview.as_view(), name='list_productreviews'),
    path('productreviews/<int:pk>', DetailProductReview.as_view(), name='singleproductreview'),


    path('List_carts/', ListCart.as_view(), name='list_carts'),
    path('Create_carts/', CreateCart.as_view(), name='create_carts'),
    
    path('cart/<int:pk>', DetailCart.as_view(), name='singlecarts'),

    path('cart/update-status/<int:pk>/', UpdateCartStatus.as_view(), name='cartstatus'),

    path('user/<int:user_pk>/orders/', UserOrdersView.as_view(), name='user-cart'),

    path('user/<int:user_pk>/order/<int:order_pk>/', UserOrdersDetail.as_view(), name='singleusercart'),


    path('profiles/', ListProfile.as_view(), name='profiles'),
    path('profiles/<int:pk>', DetailProfile.as_view(), name='singleprofile'),
]
