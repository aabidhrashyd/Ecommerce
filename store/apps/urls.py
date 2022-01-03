from django.urls import path
from . import views

urlpatterns = [
    path('', views.apps, name='apps'),
    path('contact', views.contact , name='contact'),
    path('detail', views.detail , name='detail'),
    path('shop', views.shop , name='shop'),
    path('checkout', views.checkout , name='checkout'),
    path('cart', views.cart , name='cart'),
    path('register', views.register , name='register'),
    path('login', views.login_view , name='login'),
    path('logout/', views.logout_view, name='logout'),



  
]




