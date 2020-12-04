from django.shortcuts import render
from .models import Product
# Create your views here.


def all_products(request):
    """ This will show the art and search queries aswell """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
