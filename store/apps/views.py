from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
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

def products(request):
    return render(request, 'shop.html')


def shop(request):
     products = Product.objects.all()
     return render(request, 'shop.html', {'products': products})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            return redirect('apps')  # Redirect to the index page after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('apps')  # Redirect to the index page after successful login
        else:
            messages.error(request, 'Invalid username or password')  # Show error message if login fails
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Log the user in after successful registration
#             login(request, user)
#             return redirect('apps')  # Redirect to a home page or wherever appropriate
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('apps')  # Redirect to a home page or wherever appropriate
#     else:
#         form = AuthenticationForm()

#     return render(request, 'login.html', {'form': form})

