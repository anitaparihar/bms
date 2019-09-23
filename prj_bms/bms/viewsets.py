from django.shortcuts import render
from .models import Category, Brand, Shop, Invoice
from rest_framework import viewsets, filters
from .serializers import CategorySerializer, BrandSerializer, ShopSerializer, InvoiceSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('category_id')
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_id', 'category_name', 'category_description')


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('brand_id', 'brand_name', 'brand_description')

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('shop_name', 'shop_owner', 'shop_address')

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('invoice_transaction_id',)
