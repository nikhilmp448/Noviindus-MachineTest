
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.add_product,name="add_product"),
    path('edit_product/<str:slug>/', views.edit_product,name='product_edit'),
    path('delete-adminprod/<str:slug>',views.delete_adminprod,name="delete-adminprod"),
    path('product-details/<str:slug>/',views.view_product,name="product-details"),
]
