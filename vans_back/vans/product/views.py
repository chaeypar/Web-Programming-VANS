from rest_framework import generics

from .serializers import ProductSerializer

class ProductCreateList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = None
    pagination_class = None
    
class ProductDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = None
