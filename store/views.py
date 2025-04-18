from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return HttpResponse('Hello World')
    # return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return HttpResponse('Hello World')
    # return render(request, 'store/product_detail.html', {'product': product})
