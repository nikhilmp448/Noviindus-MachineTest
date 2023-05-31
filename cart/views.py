from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from . models import OrderItem
from product.models import Product

# Create your views here.

def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if OrderItem.objects.filter(user=request.user.id,product_id=prod_id):
                    return JsonResponse({'status':"Product Already in cart"})
                else:
                    prod_qty = int(request.POST.get('quantity'))
                    OrderItem.objects.create(user=request.user, product_id=prod_id , quantity=prod_qty)
                    return JsonResponse({'status':"Product added successfully"})  
            else:
                return JsonResponse({'status':"no such product found"})
        else:
            return JsonResponse({'status':"login required"})
    return redirect('home')


@login_required(login_url='login')
def viewcart(request):
        carts =OrderItem.objects.filter(user = request.user)
        context ={'carts':carts}
        return render(request,"cart.html",context)
    

def updatecart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if OrderItem.objects.filter(user=request.user,product_id=prod_id):
            prod_qty = int(request.POST.get('quantity'))
            
            cart = OrderItem.objects.get(  product_id=prod_id ,user=request.user)
            cart.quantity=prod_qty
            cart.save()
            return JsonResponse({'status':"updated"})
        
    return redirect('home')


def deletecart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if OrderItem.objects.filter(user=request.user,product_id=prod_id):
            cart_item =  OrderItem.objects.get (  product_id=prod_id , user=request.user )
            cart_item.delete()
        return JsonResponse({'status':"item removed"})
    return redirect('home')