import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField



User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Color(models.Model):
    name = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=5)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name   


class Shipping(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return '{} || #{}'.format(self.name, self.price)   



class Product(models.Model):
    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    initial_price = models.FloatField(default=0)
    discount_percent = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)
    sku = models.CharField(max_length=10, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)
    size = models.ManyToManyField(Size, blank=True)
    author = models.CharField(max_length=100, blank=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    pages = models.PositiveIntegerField(default=0, blank=True, null=True)
    description = models.TextField(max_length=250)
    image1 = models.URLField()
    image2 = models.URLField(null=True, blank=True)
    image3 = models.URLField(null=True, blank=True)
    image4 = models.URLField(null=True, blank=True)
    status = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{} {}'.format(self.tag, self.name)

    @property
    def current_price(self):
        if self.discount_percent > 0:
            discounted_price = self.initial_price - self.initial_price * self.discount_percent / 100
            return discounted_price
        else:
            price_now = self.initial_price
            return price_now
            


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_item', on_delete=models.CASCADE)
    product = models.OneToOneField(Product, related_name='cart_product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    shipping_location = models.ForeignKey(Shipping, on_delete=models.CASCADE, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    @property
    def shipping(self):
        if self.shipping_location.price > 0:
            location = self.shipping_location.price
        return location

    @property
    def total(self):
        if self.product.discount_percent > 0:
            price_now = self.product.initial_price - self.product.initial_price * self.product.discount_percent / 100

            total = price_now * self.quantity

        else:
            price_now = self.product.initial_price
            total = price_now * self.quantity
            return total
        return total

    @property
    def grand_total(self):
        if self.product.discount_percent > 0:
            price_now = self.product.initial_price - self.product.initial_price * self.product.discount_percent / 100
            
            total = price_now * self.quantity + self.shipping_location.price

        else:
            price_now = self.product.initial_price
            total = price_now * self.quantity + self.shipping_location.price
            return total
        return total



# class Cart(models.Model):

#     STATUS = (
#         ('PENDING', 'Pending'),
#         ('IN_TRANSIT', 'In-transit'),
#         ('DELIVERED', 'Delivered')
#     )
    
#     cart_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
#     color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
#     size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
#     shipping_location = models.ForeignKey(Shipping, on_delete=models.CASCADE, default=0)
#     status = models.CharField(max_length=20, choices=STATUS, default=STATUS[0][0])
#     updated_on = models.DateTimeField(auto_now=True)
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['cart_id', '-created_on']

#     def __str__(self):
#         return str(self.cart_id)

#     @property
#     def total(self):
#         if self.order_item.discount_percent > 0:
#             price_now = self.order_item.initial_price - self.order_item.initial_price * self.order_item.discount_percent / 100

#             total = price_now * self.quantity

#         else:
#             price_now = self.order_item.initial_price
#             total = price_now * self.quantity
#             return total
#         return total

#     @property
#     def grand_total(self):
#         if self.order_item.discount_percent > 0:
#             price_now = self.order_item.initial_price - self.order_item.initial_price * self.order_item.discount_percent / 100

#             total = price_now * self.quantity + self.shipping_location.price

#         else:
#             price_now = self.order_item.initial_price
#             total = price_now * self.quantity + self.shipping_location.price
#             return total
#         return total




class ProductReview(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=150)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user_id)

    class Meta:
        ordering = ['user_id', '-created_on']



class Profile(models.Model):

    GENDER = {
        ('Male', 'Male'),
        ('Female', 'Female')
    }


    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=20)
    phone_number = PhoneNumberField(null=False, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user_id)
    

class Address(models.Model):
    
    COUNTRY = {
        ('Nigeria', 'Nigeria')
    }

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=150)
    zipcode = models.PositiveBigIntegerField(default=0)
    country = models.CharField(choices=COUNTRY, max_length=20)
    state = models.CharField(max_length=20)
    phone_number = PhoneNumberField(null=False, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)