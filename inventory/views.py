# en inventory/views.py

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Transaction
from django.db.models import Sum
from .serializers import ProductSerializer, TransactionSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class StockListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        stock_data = []
        for product in products:
            total_in = product.quantity
            total_in += Transaction.objects.filter(product=product, transaction_type='IN').aggregate(total_in=Sum('quantity'))['total_in'] or 0
            total_out = Transaction.objects.filter(product=product, transaction_type='OUT').aggregate(total_out=Sum('quantity'))['total_out'] or 0
            current_stock = total_in - total_out
            stock_data.append({
                'product_name': product.name,
                'current_stock': current_stock
            })
        return Response(stock_data)
