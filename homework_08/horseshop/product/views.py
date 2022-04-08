from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from product.models import Product

def index(request):
    context = {
        'title': 'Home page'
    }
    return render(request, 'product/index.html', context)


class ProductDetailView(DetailView):
    model = Product

class ProductsListView(ListView):
    model = Product
