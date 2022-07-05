from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=250)
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



class Product(models.Model):
    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    initial_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
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



class Cart(models.Model):

    STATUS = (
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In-transit'),
        ('DELIVERED', 'Delivered')
    )
    cart_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS[0][0])
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['cart_id', '-created_on']

    def __str__(self):
        return str(self.cart_id)






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

    COUNTRY = {
        ('Nigeria', 'Nigeria')
    }

    GENDER = {
        ('Male', 'Male'),
        ('Female', 'Female')
    }


    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    zipcode = models.PositiveBigIntegerField(default=0)
    country = models.CharField(choices=COUNTRY, max_length=20)
    state = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER, max_length=20)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user_id)
    
