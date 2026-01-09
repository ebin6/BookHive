from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bookapi.serializers import AuthorSerializer
from manager.models import Author
# Create your views here.

class AuthorAPI(ModelViewSet):
    serializer_class=AuthorSerializer
    queryset=Author.objects.all()