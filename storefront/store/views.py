from multiprocessing import context
from operator import imod
import stat
from xml.dom.minidom import Element
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from store import serializers
from rest_framework.decorators import APIView
from store.models import Collection, Product
from store.serializers import CollectionSerializer, ProductSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class ProductViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['collection_id']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields  = ['title']
    ordering_fields = ['unit_price']
    
    
class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    
