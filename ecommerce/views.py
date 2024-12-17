from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UsersTable, ProductsTable, LikedProductsTable, CartTable, OrderTable
from .serializers import UsersSerializer, ProductsSerializer, LikedProductsSerializer,CartSerializer, OrdersSerializer
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = UsersTable.objects.all()
    serializer_class = UsersSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = ProductsTable.objects.all()
    serializer_class = ProductsSerializer
    @action(methods=["GET"],detail=True, url_path="liked")
    def get_data(self,request, *args, **kwargs):
        data=self.get_object().product_liked
        liked_data=LikedProductsSerializer(data,many=True).data
        return Response(self.get_object().product_liked.count())


class LikedViewSet(viewsets.ModelViewSet):
    queryset = LikedProductsTable.objects.all()
    serializer_class = LikedProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_Liked','is_Disliked']
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        query = super().get_queryset()
        query_params = self.request.query_params
        if "is_liked" in query_params and query_params.get('is_liked') in ['True','true']:
            query = query.filter(is_Liked=True)
        return query
    
    @action(methods=["GET"],detail=False, url_path="liked")
    def getIsLiked(self,request,*args, **kwargs):
        queryset=self.get_queryset().filter(is_Liked=True)
        return Response(self.serializer_class(queryset,many=True).data)


class CartViewset(viewsets.ModelViewSet):
    queryset = CartTable.objects.all()
    serializer_class = CartSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = OrderTable.objects.all()
    serializer_class = OrdersSerializer    

def index(request):
    return HttpResponse("hello welcome to the dome")     