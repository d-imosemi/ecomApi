from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Color(models.Model):
    name = models.CharField(max_length=15)


    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=5)


    def __str__(self):
        return self.name     




class Book(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, related_name='books')
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField(default=0)
    initial_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    tag = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    initial_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=10, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)
    size = models.ManyToManyField(Size, blank=True)
    description = models.TextField()
    image = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.tag, self.name)


class Cart(models.Model):
    cart_id = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    books = models.ManyToManyField(Book)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['cart_id', '-created_on']

    def __str__(self):
        return str(self.cart_id)




class BookReview(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True)
    review = models.TextField(max_length=250)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user_id)



class ProductReview(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    review = models.TextField(max_length=250)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user_id)
    