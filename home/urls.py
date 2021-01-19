from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('bayilerimiz/', views.bayilerimiz, name="bayilerimiz"),
    path('login/', views.loginPage, name="loginPage"),
    path('cikisyap/', views.cikisyap, name="cikisyap"),
    path('signIn/',views.signIn,name="signIn"),
    path('urunler/',views.urunler,name="urunler")
]
