from django.urls import path
from . import views

urlpatterns = [
    path('', views.bayi, name="bayi"),
    path('bayisatis/',views.bayisatis,name="bayisatis"),
    path('bayisiparis/',views.siparisEt,name="siparisEt"),
    path('satışSil/<int:id>', views.satışSil,name="satışSil"),
    path('bayibakim/',views.bayiBakim, name="bayiBakim"),
    path('bakimSil/<int:id>', views.bakimSil,name="bakimSil"),
    path('bilgilendirme/', views.bilgilendirme, name = "bilgilendirme"),
    path('bayikayıt/', views.bayiKayıt, name="bayiKayıt"),
    path('satışYap', views.satışEkle, name="satışEkle"),
    path('müşteriEkle', views.müşteriEkle, name="müşteriEkle"),
    path('bakımYap/<int:id>', views.bakımYap, name="bakımYap"),
    path('siparişVer', views.siparişVer, name='siparişVer'),
    path('teslimAl/<int:id>', views.teslimAl, name='teslimAl'),
    path('siparişTamamla', views.siparişTamamla, name='siparişTamamla'),
    path('siparişSil/<int:id>', views.siparişSil, name='siparişSil'),
    
]