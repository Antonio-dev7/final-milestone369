from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    """ This will show the art and search queries aswell """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ showing individual art  """

    product = get_object_or_404(Product, pk=product_id)  # only want to return 1 art work

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
