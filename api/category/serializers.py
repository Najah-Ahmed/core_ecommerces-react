from rest_framework import serializers
from .models import Category

# *** HyperlinkedModelSerializer vs ModelSerializer


class CategorySerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'description', 'url')
