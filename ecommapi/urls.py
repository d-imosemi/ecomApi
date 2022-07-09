from django.urls import path
from .views import *

urlpatterns = [
    path('', HelloAuthView.as_view(), name='home'),
    path('list_categories/', ListCategory.as_view(), name='list_categories'),
    path('Create_category/', CreateCategory.as_view(), name='create_category'),
    path('category/<int:pk>/', DetailCategory.as_view(), name = 'single_category'),

    # path('list_colors/', ListColor.as_view(), name='list_colors'),
    path('create_color/', CreateColor.as_view(), name='create_color'),
    path('color/<int:pk>/', DetailColor.as_view(), name = 'singlecolor'),


    # path('list_sizes/', ListSize.as_view(), name='list_sizes'),
    path('create_size/', CreateSize.as_view(), name='Create_size'),
    path('size/<int:pk>/', DetailSize.as_view(), name = 'singlesize'),


    path('list_products/', ListProduct.as_view(), name='list_products'),
    path('create_product/', CreateProduct.as_view(), name='create_product'),
    path('product/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),


    path('productreview/', CreateProductReview.as_view(), name='productreview'),
    # path('list_productreviews/', ListProductReview.as_view(), name='list_productreviews'),
    path('productreview/<int:pk>/', DetailProductReview.as_view(), name='singleproductreview'),


    path('List_carts/', ListCart.as_view(), name='list_carts'),
    path('Create_cart/', CreateCart.as_view(), name='create_cart'),
    
    path('cart/<int:pk>/delete/', DeleteDetailCart.as_view(), name='Delete_singlecart'),
    path('cart/<int:pk>/update/', UpdateDetailCart.as_view(), name='Update_singlecart'),

    path('cart/update-status/<int:pk>/', UpdateCartStatus.as_view(), name='cartstatus'),

    path('user/<int:user_pk>/orders/', UserOrdersView.as_view(), name='user-cart'),

    path('user/<int:user_pk>/order/<int:order_pk>/', UserOrdersDetail.as_view(), name='singleusercart'),



    path('profile/<int:pk>', DetailProfile.as_view(), name='singleprofile'),
]
