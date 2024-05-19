from django.db import models
from django.contrib.auth.models import AbstractUser
from .myusermanager import MyUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

#user data for login and signup - CUSTOMERS ------------------------

class MyUser(AbstractUser):
    user = models.OneToOneField('self', on_delete=models.CASCADE, unique=True, related_name='MyUser', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)    
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)
    is_premium_member = models.BooleanField(default=False)
    mobile = models.CharField(max_length=11, unique=True)
    otp = models.IntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=100)
    date_modified = models.DateTimeField(auto_now=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    backend = 'custom_loggin.mybackend.ModelBackend'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def get_age(self):
        if self.date_of_birth:
            today = datetime.date.today()
            birth_date = self.date_of_birth
            age = today.year - birth_date.year 
            return age
        
    def get_full_address(self):
        return self.address

    def __str__(self):
        return self.mobile


# Create a user Profile by default when user signs up

# Update the create_profile function to perform actions after MyUser instance creation
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Perform actions after MyUser instance creation here
        pass

# Connect the signal to the function
post_save.connect(create_profile, sender=MyUser)
