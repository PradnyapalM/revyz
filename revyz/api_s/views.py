from django.shortcuts import render
from rest_framework import viewsets

from .pagination import CustomPagination
from .serializers import api_sSerializer
from .models import api_s
from rest_framework import filters

# Create your views here.

class api_sView(viewsets.ModelViewSet):
    serializer_class = api_sSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['Tech_skill','City']
    queryset = api_s.objects.all()
