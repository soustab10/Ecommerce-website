from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    
class Category(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_title=models.CharField(max_length=255)
    c_description=models.TextField()
    
    def get_absolute_url(self):
        return reverse("category_list")

    def __str__(self):
        return self.title
    
class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_rating = models.DecimalField(max_digits=5, decimal_places=1)
    p_description = models.CharField(max_length=200)
    p_stock = models.IntegerField()
    p_brand = models.CharField(max_length=100)
    p_price= models.DecimalField(max_digits=10, decimal_places=2,null=True)
    p_category=models.ForeignKey('Category', on_delete=models.CASCADE,null=True)
    p_image = models.ImageField(upload_to="product_image/")
    def __str__(self):
        return self.p_name


   
class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    
    
class Review(models.Model):
    r_customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null=True)
    r_rating = models.DecimalField(max_digits=5, decimal_places=1)
    r_description=models.CharField(max_length=500)
    r_date= models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    


    
