from rest_framework import viewsets, generics
from .serializers import CategorySerializers
from .models import Category

# *** viewsets vs generics


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializers


class CategoryGenerics(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializers
