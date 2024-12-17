from rest_framework import serializers
from .models import ProductsTable, UsersTable, LikedProductsTable, CartTable, OrderTable

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsersTable
        fields='__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsTable
        fields = '__all__'   
        
class LikedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedProductsTable
        fields = '__all__'   
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartTable
        fields = '__all__'
           
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTable
        fields = '__all__'
        