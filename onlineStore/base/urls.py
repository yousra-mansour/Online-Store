from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('prodact/<str:pk>', views.shopItem, name='prodact'),
    path('login/', views.userLogin, name='Login'),
    path('reg/', views.userReg, name='reg'),

]
