
from .models import OrderItem


def counter(request):
    count = 0
    if request.user.is_authenticated:
        cart = OrderItem.objects.filter(user=request.user)
        
        for item in cart:
            count+=item.quantity
    return dict(count=count)





 