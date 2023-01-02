from django.shortcuts import render
from .models import Products

def index(request):
    prod = Products.objects.all()
    context = {'Products':prod}
    return render(request, 'home/index.html', context)

def prod_details(request,pk):
    prod = Products.objects.get(id = pk)
    return render(request, 'home/product-details.html',{'prod_detail':prod})