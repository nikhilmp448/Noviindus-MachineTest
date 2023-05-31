from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart',views.addtocart,name="add-to-cart"),
    path('update-cart',views.updatecart,name="update-cart"),
    path('delete-cart',views.deletecart,name="delete-cart"),
    path('viewcart/',views.viewcart,name="viewcart")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
