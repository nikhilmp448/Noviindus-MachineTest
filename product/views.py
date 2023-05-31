from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.forms import AddProductForm
from product.models import Product

# Create your views here.
@login_required(login_url='login')
def add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddProductForm(request.POST,request.FILES)
            if form.is_valid():
                print('valid')
                form.save()
                print('data saved successfully')
                return redirect('home')
            else:
                print('product not added')
                messages.info(request,'product not added')
    else:
        return redirect("login")

def view_product(request,slug ):
    item =Product.objects.get(slug=slug)
    context= {
        'item':item
        }
    return render(request,'product_details.html',context)

@login_required(login_url='admin_signin')
def edit_product(request, slug) :
    if request.user.is_authenticated:
        product = Product.objects.get(slug=slug)
        if request.method == 'POST' :
            form = AddProductForm(request.POST, request.FILES, instance=product)   
            if form.is_valid() :
                form.save()
                return redirect('home')
            
        form = AddProductForm(instance=product)
        context = {'form' : form}
        return render(request, 'edit_product.html', context)
    else:
        return redirect("login")

@login_required(login_url='admin_signin')
def delete_adminprod(request,slug):
    if request.user.is_authenticated:
        adminprod =  Product.objects.get(slug=slug)
        adminprod.delete()
        return redirect('home')
    else:
        return redirect("login")