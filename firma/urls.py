from django.urls import path
from . import views

urlpatterns= [
    path('', views.firma, name="firma"),
    path('siparisler/', views.siparisler, name="siparisler"),
    path('odemeler/', views.odemeler, name="odemeler"),
    path('urunler/', views.urunler, name="urunler"),
    path('bayiler/', views.bayiler, name="bayiler"),
    path('receteler/',views.receteler, name="receteler"),
    path('hammaddeler/',views.hammaddeler,name="hammaddeler"),
    path("bayiSil/<int:id>", views.bayiSil, name="bayiSil"),
    path("bayiOnayla/<int:id>", views.bayiOnayla, name="bayiOnayla"),
    path("ürünGöster/<int:id>", views.siparişÜrün, name="siparişÜrün"),
    path('firmaSiparisSil/<int:id>', views.firmaSiparisSil,name="firmaSiparisSil"),
    path('firmaUrunSil/<int:id>',views.firmaUrunSil,name="firmaUrunSil"),
    path('firmaOdemeSil/<int:id>',views.firmaOdemeSil,name="firmaOdemeSil"),
    path("ürünEkle/", views.ürünEkle, name="ürünEkle"),
    path("ödemeEkle/", views.ödemeEkle, name="ödemeEkle"),
    path('siparişOnayla/<int:id>', views.siparişOnayla, name="siparişOnayla"),
    path('ürünGüncelle/<int:id>', views.ürünGüncelle, name= "ürünGüncelle"),
    path('reçeteEkle/', views.reçeteEkle, name='reçeteEkle'),
    path('hammaddeEkle/', views.hammaddeEkle, name='hammaddeEkle'),
    path('reçeteGüncelle/<int:id>', views.reçeteGüncelle, name= "reçeteGüncelle"),
    path('reçeteSil/<int:id>', views.reçeteSil, name= "reçeteSil"),
    path('hammaddeGüncelle/<int:id>', views.hammaddeGüncelle, name='hammaddeGüncelle'),
    path('hammaddeSil/<int:id>', views.hammaddeSil, name= "hammaddeSil"),

]