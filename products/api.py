# views.py : API

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductListSerializer,ProductDetailSerializer , BrandListSerializer,BrandDetailSerializer
from .models import Product , Brand
from .mypagination import CustomPagination
from .myfilter import CustomProductFIlter



# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()   # list 
#     data = ProductSerializer(products,many=True,context={"request":request}).data   # json 
#     return Response({'products':data})



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand','quantity']
    # search_fields = ['name','subtitle','description']
    ordering_fields = ['price','quantity','name']
    filterset_class = CustomProductFIlter
    permission_classes = [IsAuthenticated]
    
    
    
class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    
    
class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer