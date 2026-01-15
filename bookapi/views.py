from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bookapi.serializers import AuthorSerializer
from manager.models import Author
from .pagination import AuthorPagination
# Create your views here.

class AuthorAPI(ModelViewSet):
    serializer_class=AuthorSerializer
    queryset=Author.objects.all()
    pagination_class=AuthorPagination
    search_fields=['name']