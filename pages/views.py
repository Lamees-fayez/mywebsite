from django.shortcuts import render
from .models import Product,Login
from .form import Login_Form


# Create your views here.
from .models import Product

def first(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'page/first.html', context)
def second(request):
    products = Product.objects.filter(id=1)
    context = {'products': products}
    return render(request, 'page/second.html',context)
def Loginn(request.POST):
    if request.method='POST'
        data =Login_Form(request.POST)
        if data.is_valid():
            data.save()



    return render(request, 'page/login.html',{})