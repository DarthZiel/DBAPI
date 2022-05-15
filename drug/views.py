from rest_framework.permissions import IsAuthenticated

from .serializer import DrugSerializer
from django.http import HttpResponse
from .models import Drug
from rest_framework.filters import SearchFilter

from rest_framework import viewsets

def index(requests):
    return HttpResponse('Application programming interface')

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','price']
    permission_classes = (IsAuthenticated,)
