from rest_framework import viewsets
from .serializers import ProductSerializer

from .models import Products


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductSerializer
