from django.db import models
from cart.models import Cart
from custom_loggin.models import MyUser  

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='checkout_orders')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
