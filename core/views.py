from django.shortcuts import render
from .models import Sipariş_Ürün

# Create your views here.

def ürünGöster(request,id):
    s_ü = Sipariş_Ürün.objects.filter(sipariş_id=id)
    context = {'ürünler':s_ü}
    return render(request,"core/urungoster.html",context)