from django.urls import path
from . import views

urlpatterns = [
    path('', views.apps, name='apps'),
    path('contact', views.contact , name='contact'),
    path('detail', views.detail , name='detail')
]
