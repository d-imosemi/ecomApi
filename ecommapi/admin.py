from django.contrib import admin

from .models import *



class ProductReviewInline(admin.StackedInline):
    model = ProductReview
    extra = 0




class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name', 'updated_on', 'created_on',)
    list_display = ('name', 'category', 'author', 'initial_price', 'current_price', 'stock',)
    inlines = [
            ProductReviewInline,
        ]


class ProductReviewAdmin(admin.ModelAdmin):
    list_filter = ('id', 'created_on',)
    list_display = ('user_id', 'review', 'product', 'rating', 'created_on',)


class CartItemAdmin(admin.ModelAdmin):
    list_filter = ('cart', 'created_on',)
    list_display = ('cart', 'quantity', 'shipping', 'total', 'grand_total', 'created_on',)




admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview,  ProductReviewAdmin)
admin.site.register(Size)
admin.site.register(Profile)
admin.site.register(Shipping)

admin.site.register(Address)

admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)

admin.site.register(Order)
admin.site.register(OrderItem)




