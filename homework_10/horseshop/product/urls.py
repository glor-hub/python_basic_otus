from django.urls import path

import product.views as product

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/', product.ProductDetailView.as_view(), name='detail'),
    path('list/', product.ProductsListView.as_view(), name='list'),
]
