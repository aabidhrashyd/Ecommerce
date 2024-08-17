from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def apps(request):
    #return HttpResponse("Hello world!")
    return render(request, 'index.html')

def contact(request):
    #return HttpResponse("Hello world!")
    return render(request, 'contact.html')

def detail(request):
    #return HttpResponse("Hello world!")
    return render(request, 'detail.html')

def shop(request):
    #return HttpResponse("Hello world!")
    return render(request, 'shop.html')

def checkout(request):
    #return HttpResponse("Hello world!")
    return render(request, 'checkout.html')

def contact(request):
    #return HttpResponse("Hello world!")
    return render(request, 'contact.html')

def cart(request):
    #return HttpResponse("Hello world!")
    return render(request, 'cart.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page.
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})