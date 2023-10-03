
from django.urls import path
from . import views


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name="index"),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name= 'register'),
    path('checkout/', views.checkout, name= 'checkout'),
]