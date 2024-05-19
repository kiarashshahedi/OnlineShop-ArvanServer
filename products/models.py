from django.db import models
from myshop import settings
import datetime
from custom_loggin.models import MyUser

#Products Category
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    
    
#All Products
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/')
    inventory = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    total_ratings = models.IntegerField(default=0)
    
    # adding sale 
    in_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=9, decimal_places=3)    
    
    def update_ratings(self):
        reviews = self.reviews.all()
        total_ratings = reviews.count()
        if total_ratings > 0:
            sum_ratings = sum(review.rating for review in reviews if review.rating is not None)
            self.average_rating = sum_ratings / total_ratings
        else:
            self.average_rating = 0.0
        self.total_ratings = total_ratings
        self.save()
    
    def total_orders(self):
        return self.order_set.filter(status=True).count()

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image of {self.product.name}"
    
    
#the rate of the product
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)  # Rating (1 to 5 stars)
    comment = models.TextField(null=True, blank=True)  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = []


    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"

#Customers Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='customer_orders', related_query_name='customer_order')  # Add related_name and related_query_name
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
    
