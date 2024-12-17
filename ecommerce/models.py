from django.db import models

class UsersTable(models.Model):
    """models for all the users"""
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    isDeleted=models.BooleanField(default=False)
    addresses=models.JSONField(default=list)
    liked_products=models.JSONField([{"p_id":models.IntegerField(max_length=50),"p_name":models.CharField(max_length=100)}])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductsTable(models.Model):
    p_name=models.CharField(max_length=200)
    p_desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class LikedProductsTable(models.Model):
    p_id=models.IntegerField(max_length=50)
    p_name=models.CharField(max_length=200)
    total_likes=models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class CartTable(models.Model):
    user_id=models.IntegerField(max_length=50)
    products=models.JSONField([{"product_id":models.IntegerField(max_length=50), "p_name":models.CharField(max_length=100),"qnty":models.IntegerField(max_length=2)}])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class OrderTable(models.Model):
    user_id=models.IntegerField(max_length=50)
    products=models.JSONField([{"product_id":models.IntegerField(max_length=50), "p_name":models.CharField(max_length=100),"qnty":models.IntegerField(max_length=2), "cost":models.IntegerField(max_length=5)}])
    address=models.TextField()
    total_cost=models.IntegerField(max_length=5)
    is_delivered=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    