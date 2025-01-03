from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import ListAPIView

# Create your views here. 
class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
