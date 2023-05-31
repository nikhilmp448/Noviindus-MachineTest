from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.shortcuts import redirect, render
from django.contrib import messages
from product.forms import AddProductForm
# Create your views here.

@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    
    if request.user.is_superadmin:
        form = AddProductForm()
        return render(request, 'admin.html',{'form':form,'products':products})
    return render(request, 'home.html',context)
