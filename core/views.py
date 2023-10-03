from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from product.models import *
from user.models import *
from order.models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages



# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'homepage/index.html', context)


def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, is_completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'homepage/cart.html', context)


def base(request):
    context= {}
    return render(request, 'homepage/base.html', context)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, is_completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
    products = Product.objects.all()
    context = {'searched': searched, 'keys': keys, 'products': products}
    return render(request, 'homepage/search.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'user or password not connect!')
    context ={}
    return render(request, 'homepage/login.html', context)


def register(request):
    form = CustomerUser()
    if request.method == 'POST':
        form = CustomerUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {"form": form}
    return render(request, 'homepage/register.html', context)


def checkout(request):
    context = {}
    return render(request, 'homepage/checkout.html', context)