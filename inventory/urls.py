# en inventory/urls.py

from django.urls import path
from .views import ProductListCreateAPIView, TransactionListCreateAPIView, StockListAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('stock/', StockListAPIView.as_view(), name='stock-list-api'),
]
