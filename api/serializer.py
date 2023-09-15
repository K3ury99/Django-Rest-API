from rest_framework import serializers 
from .models import Libros


class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        # fields = ('fullname','age')
        fields = '__all__'
