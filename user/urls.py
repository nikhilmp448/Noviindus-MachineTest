
from django.urls import path
from . import views
from home import views as homeView

urlpatterns = [
    
    path('login/',views.loginpage,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logoutuser,name='logout'),
]


