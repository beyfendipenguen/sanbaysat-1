from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ürünEkleForm, ödemeEkleForm, ürünGüncelleForm, reçeteEkleForm, hammaddeEkleForm, reçeteGüncelleForm, hammaddeGüncelleForm
from core.models import Sipariş, Ürün, Ödeme, Bayi, Sipariş_Ürün, Hammadde, Reçete, Müşteri, Bakım
"""
def modelAdıEkle(request):
    if request.method == "POST":
        form = modelAdıEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            return redirect("Yönlendirilecek Sayfa")
    
    else:
        form = modelAdıEkleForm()
    context = {"form":form}
    return render(request,"tempalteAdı",context)

def modelGüncelle(request,id):
    model=Model.objects.get(pk=id)
    if request.method == "POST":
        form = modelGüncelleForm(request.POST)
        if form.is_valid():
           
            return redirect("")
    else:
        form = modelGüncelleForm(instance=model)
    context = {"form":form}
    return render(request,"template",context)



""" 
def reçeteGüncelle(request,id):
    reçete=Reçete.objects.get(pk=id)
    if request.method == "POST":
        form = reçeteGüncelleForm(request.POST)
        if form.is_valid():
            reçete.ürün = form.cleaned_data['ürün']
            reçete.hammadde = form.cleaned_data['hammadde']
            reçete.miktar = form.cleaned_data['miktar']
            reçete.save()
            return redirect("firma")
    else:
        form = reçeteGüncelleForm(instance=reçete)
    context = {"form":form}
    return render(request,"firma/reçeteGüncelle.html",context)

def hammaddeGüncelle(request,id):
    hammadde=Hammadde.objects.get(pk=id)
    if request.method == "POST":
        form = hammaddeGüncelleForm(request.POST)
        if form.is_valid():
            hammadde.adı = form.cleaned_data['adı']
            hammadde.depodaki_miktar = form.cleaned_data['depodaki_miktar']
            hammadde.tedarik_süresi = form.cleaned_data['tedarik_süresi']
            hammadde.kritik_seviye = form.cleaned_data['kritik_seviye']
            hammadde.save()
            return redirect("firma")
    else:
        form = hammaddeGüncelleForm(instance=hammadde)
    context = {"form":form}
    return render(request,"firma/hammaddeGüncelle.html",context)


def reçeteEkle(request):
    if request.method == "POST":
        form = reçeteEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            form.save()
            return redirect("firma")
    
    else:
        form = reçeteEkleForm()
    context = {"form":form}
    return render(request,"firma/reçeteEkle.html",context)

def reçeteSil(request,id):
    reçete = Reçete.objects.get(pk=id)
    reçete.delete()
    return redirect('firma')
    
def hammaddeSil(request,id):
    hammadde = Hammadde.objects.get(pk=id)
    hammadde.delete()
    return redirect('firma')

def hammaddeEkle(request):
    if request.method == "POST":
        form = hammaddeEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            form.save()
            return redirect("firma")
    
    else:
        form = hammaddeEkleForm()
    context = {"form":form}
    return render(request,"firma/hammaddeEkle.html",context)

def ürünGüncelle(request,id):
    ürün=Ürün.objects.get(pk=id)
    if request.method == "POST":
        form = ürünGüncelleForm(request.POST)
        if form.is_valid():
            urun = Ürün.objects.get(pk=id)
            urun.adı= form.cleaned_data['adı']
            urun.kapak  = form.cleaned_data['kapak']
            urun.genişlik  = form.cleaned_data['genişlik']
            urun.yükseklik  = form.cleaned_data['yükseklik']
            urun.kapasite  = form.cleaned_data['kapasite']
            urun.voltaj  = form.cleaned_data['voltaj']
            urun.ağırlık  = form.cleaned_data['ağırlık']
            urun.bakım_aralığı  = form.cleaned_data['bakım_aralığı']
            urun.fiyat  = form.cleaned_data['fiyat']
            urun.save()
            return redirect("firma")
    else:
        form = ürünGüncelleForm(instance=ürün)
    context = {"form":form}
    return render(request,"firma/ürünGüncelle.html",context)

def siparişOnayla(request,id):
    sipariş = Sipariş.objects.get(pk=id)
    if sipariş.durum == 'b':
        sipariş.durum='o'
        sipariş.sipariş_takibi = 'h'
        if üret(sipariş):
            sipariş.save()
        return redirect('firma')
    elif sipariş.sipariş_takibi== 'h':
        sipariş.sipariş_takibi = 'y'
        sipariş.save()
        return redirect('firma')
    else:
        return redirect('firma')



def üret(sipariş):
    #reçete, sipraişürün, hammadde
    sipariş_ürün = Sipariş_Ürün.objects.filter(sipariş=sipariş)

    for s_ü in sipariş_ürün:
        reçeteler = Reçete.objects.filter(ürün=s_ü.ürün)
        for r in reçeteler:
            hammadde = r.hammadde
            hammadde.depodaki_miktar-=r.miktar*s_ü.adet
            if hammadde.depodaki_miktar > hammadde.kritik_seviye:
                hammadde.save()
            else:
                return False
    return True

def ödemeEkle(request):
    if request.method == "POST":
        form = ödemeEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            form.save()
            return redirect("firma")
    
    else:
        form = ödemeEkleForm()
    context = {"form":form}
    return render(request,"firma/ödemeEkle.html",context)

def ürünEkle(request):
    if request.method == "POST":
        form = ürünEkleForm(request.POST)
        if form.is_valid():
            #form bilgileri
            #model.save()
            form.save()
            return redirect("firma")
    
    else:
        form = ürünEkleForm()
    context = {"form":form}
    return render(request, "firma/ürünEkle.html", context)
        



# Create your views here.
def firma(request):
    #TODO kullanıcı girişi
    user = User.objects.get(pk=request.user.pk)
    if user is not None:
        if user.is_superuser:
            print("buyur reis şöyle geç")
        else:
            return redirect('home')
    siparişler = Sipariş.objects.all()
    ürünler = Ürün.objects.all()
    bayiler = Bayi.objects.all()
    ödemeler = Ödeme.objects.all()
    hammaddeler = Hammadde.objects.all()
    receteler = Reçete.objects.all()
    return render(request, "firma/firma.html", {"siparişler":siparişler, "ürünler":ürünler, "bayiler":bayiler,"ödemeler":ödemeler, "hammaddeler":hammaddeler, "receteler": receteler})


def siparişÜrün(request,id):
    s_ü = Sipariş_Ürün.objects.filter(sipariş_id=id)
    context = {'ürünler':s_ü}
    return render(request,"firma/urungoster.html",context)

def bayiSil(request,id):
    bayi = Bayi.objects.get(pk=id)
    kullanıcı = bayi.user
    bayi.delete()
    if Bayi.objects.filter(user_id=kullanıcı.id).__bool__() == False:
        kullanıcı.is_staff = False
        kullanıcı.save()
    return redirect("firma")
"""
def nesneSil(request,nesneadı,id):
    nesne = nesneadı.objects.get(pk=id)
    nesne.delete()
    return redirect("firma")
"""
def bayiOnayla(request,id):
    bayi = Bayi.objects.get(pk=id)
    kullanıcı = User.objects.get(pk=bayi.user.pk)
    kullanıcı.is_staff=True
    kullanıcı.save()
    bayi.aktif = True
    bayi.save()
    return redirect("firma")

def siparisler(request):
    return render(request, "firma/siparisler.html", {})

def odemeler(request):
    return render(request, "firma/odemeler.html", {})

def bayiler(request):
    return render(request, "firma/bayiler.html", {})

def urunler(request):
    return render(request, "firma/urunler.html", {})

def receteler(request):
    return render(request, "firma/recete.html", {})

def hammaddeler(request):
    return render(request, "firma/tedarik.html",{})

def siparisEkle(request):
    s = Sipariş()
    context = {}
    return render(request, "firma/siparisler.html", context)

def firmaSiparisSil(request,id):
    firmaSiparis= Sipariş.objects.get(pk=id)
    firmaSiparis.delete()
    return redirect("firma")

def firmaUrunSil(request,id):
    firmaUrun = Ürün.objects.get(pk=id)
    firmaUrun.delete()
    return redirect("firma")

def firmaOdemeSil(request,id):
    firmaOdeme = Ödeme.objects.get(pk=id)
    firmaOdeme.delete()
    return redirect("firma")