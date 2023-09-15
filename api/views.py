from rest_framework import viewsets
from .serializer import LibrosSerializer
from .models import Libros

# Create your views here.

class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer


