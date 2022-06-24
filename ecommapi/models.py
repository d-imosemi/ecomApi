from django.db import models


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

class Book(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, related_name='books')
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    initial_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image = models.URLField()
    status = models.BooleanField(default=True)
    review = models.TextField()
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
    stock = models.IntegerField()
    sku = models.CharField(max_length=10, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True, null=True)
    description = models.TextField()
    image = models.URLField()
    status = models.BooleanField(default=True)
    review = models.TextField()
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.tag, self.name)