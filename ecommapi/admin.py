from django.contrib import admin

from .models import BookReview, Cart, Category, Color, Book, Product, ProductReview, Size


class BookReviewInline(admin.StackedInline):
    model = BookReview
    extra = 0

class ProductReviewInline(admin.StackedInline):
    model = ProductReview
    extra = 0




class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name', 'date_created',)
    list_display = ('name', 'category', 'initial_price', 'current_price', 'stock',)
    inlines = [
            ProductReviewInline,
        ]

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'date_created',)
    list_display = ('title', 'category', 'author', 'initial_price', 'current_price', 'stock',)
    inlines = [
        BookReviewInline,
    ]

class BookReviewAdmin(admin.ModelAdmin):
    list_filter = ('id', 'created_on',)
    list_display = ('user_id', 'review', 'book', 'rating', 'created_on',)

class ProductReviewAdmin(admin.ModelAdmin):
    list_filter = ('id', 'created_on',)
    list_display = ('user_id', 'review', 'product', 'rating', 'created_on',)


class CartAdmin(admin.ModelAdmin):
    list_filter = ('cart_id', 'created_on',)
    list_display = ('cart_id', 'total', 'created_on',)



admin.site.register(Cart, CartAdmin)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Book, BookAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(ProductReview,  ProductReviewAdmin)
admin.site.register(Size)




