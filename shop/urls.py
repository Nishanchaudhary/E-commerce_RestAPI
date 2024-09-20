from django.urls import path
from .views import ProductList, ProductDetail, CartList, CartDetail, OrderList

urlpatterns = [
   
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

   
    path('cart/', CartList.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartDetail.as_view(), name='cart-detail'),

   
    path('orders/', OrderList.as_view(), name='order-list'),
]
