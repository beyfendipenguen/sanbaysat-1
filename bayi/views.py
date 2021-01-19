
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import Satış, Sipariş, Bayi, Bakım, Müşteri, Sipariş_Ürün
from .forms import SiparisForm, createBayi, nameForm, satışEkleForm, müşteriEkleForm, bakımYapForm, siparişÜrünForm
from dateutil.relativedelta import relativedelta
from datetime import date
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


"""
user = User.objects.get(pk=request.user.id)
bayi = Bayi.objects.get(user = user)
"""

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
""" 
def teslimAl(request,id): ##
    sipariş= Sipariş.objects.get(pk=id)
    sipariş.sipariş_takibi='t'
    sipariş.save()
    return redirect('bayi')


def siparişTamamla(request):##
    user = User.objects.get(pk=request.user.id)
    bayi = Bayi.objects.get(user = user)
    sipariş = Sipariş.objects.get(pk=request.session['sipariş_pk'])
    siparişler = Sipariş_Ürün.objects.filter(sipariş=sipariş)
    print(siparişler)
    send_email(bayi,siparişler)
    request.session['sipariş_pk'] = -1
    return redirect('bayi')

def siparişVer(request,spariş=None): ##
    user = User.objects.get(pk=request.user.id)
    bayi = Bayi.objects.get(user = user)
    if request.session['sipariş_pk'] != -1: ##
        sipariş = Sipariş.objects.get(pk=request.session['sipariş_pk'])
    else:
        sipariş = Sipariş(bayi=bayi)
    if request.method == 'POST':
        form = siparişÜrünForm(request.POST)
        if form.is_valid():
            siparişÜrün = Sipariş_Ürün(
                sipariş = sipariş,
                ürün = form.cleaned_data['ürün'],
                adet = form.cleaned_data['adet']
            )
            sipariş.save()
            request.session['sipariş_pk'] = sipariş.pk
            siparişÜrün.save()
    else:
        form = siparişÜrünForm()
    context = {'form':form}
    return render(request, 'bayi/siparişVer.html',context)

def bakımYap(request,id): #
    user = User.objects.get(pk=request.user.id)
    bayi = Bayi.objects.get(user = user)
    satış = Satış.objects.get(pk=id)
    if request.method == 'POST':
        form = bakımYapForm(request.POST)
        if form.is_valid():
            bakım = Bakım(
                satış = satış,
                açıklama = form.cleaned_data['açıklama'],
                tutar = form.cleaned_data['tutar'],
                gelecek_bakım_tarihi = date.today()+relativedelta(months=+satış.ürün.bakım_aralığı)
            )
            bakım.save()
            return redirect('bayi')
    else:
        form = bakımYapForm()
    context = {'form':form}
    return render(request, 'bayi/bakımYap.html', context)

def müşteriEkle(request):
    user = User.objects.get(pk=request.user.id)
    bayi = Bayi.objects.get(user = user)
    print(bayi)
    if request.method == "POST":
        form = müşteriEkleForm(request.POST)
        if form.is_valid():
            müşteri = Müşteri(
                adı = form.cleaned_data['adı'],
                soyadı = form.cleaned_data['soyadı'],
                adres = form.cleaned_data['adres'],
                telefon = form.cleaned_data['telefon'],
                bayi = bayi
            )
            müşteri.save()
            return redirect("satışEkle")
    
    else:
        form = müşteriEkleForm()
    context = {"form":form}
    return render(request,"bayi/müşteriEkle.html",context)

def satışEkle(request):
    user = User.objects.get(pk=request.user.pk)
    if request.method == "POST":
        bayi = request.POST.get('bayi')
        bayi = Bayi.objects.get(pk=bayi)
        print(bayi)
        form = satışEkleForm(request.POST)
        if form.is_valid():
            satış = Satış(
                bayi = bayi,
                müşteri=form.cleaned_data['müşteri'],
                ürün=form.cleaned_data['ürün'],
                satış_fiyatı = form.cleaned_data['satış_fiyatı'],
                alış_fiyatı = form.cleaned_data['alış_fiyatı'],
                ödeme_aracı =  form.cleaned_data['ödeme_aracı']
            )
            satış.save()
            return redirect("bayi")
    else:
        form = satışEkleForm()
        bayilerim = Bayi.objects.filter(user_id=user.id)
    context = {"form":form,'bayilerim':bayilerim}
    return render(request,"bayi/satışEkle.html",context)

def bayi(request):
    try:
        user = User.objects.get(pk=request.user.pk)
    except:
        return redirect('loginPage')
    if user is not None:
        if user.is_superuser:
            return redirect('firma')
        elif user.is_staff:
            bayi = Bayi.objects.get(user=user)
            bakımlar = Bakım.objects.filter(satış__bayi=bayi)
            bayisatis = Satış.objects.filter(bayi=bayi)
            siparişler = Sipariş.objects.filter(bayi=bayi)
            request.session['sipariş_pk'] = -1
            context = {"bayisatis":bayisatis,'bakımlar':bakımlar,'siparişler':siparişler}
            return render(request, "bayi/bayi.html", context)
        
        else:
            return redirect('bilgilendirme')

def bilgilendirme(request):
    return render(request, "bayi/bilgilendirme.html")

def bayiKayıt(request):
    try:
        user = User.objects.get(pk=request.user.pk)
    except:
        return redirect('loginPage') 
    if request.method == 'POST':
        form = createBayi(request.POST)
        if form.is_valid():
            adı = form.cleaned_data['adı']
            şehir = form.cleaned_data['şehir']      
            telefon = form.cleaned_data['telefon']      
            adres = form.cleaned_data['adres']
            ülke = form.cleaned_data['ülke'] 
            bayi = Bayi(
                adı=adı,
                şehir=şehir,
                telefon=telefon,
                adres = adres,
                ülke = ülke,
                user=user
            )     
            try:
                bayi.save()
                return redirect('home')
            except:
                print("kayıt hatası")
    else:
        form = createBayi()
    context = {'form':form} 
    return render(request, "bayi/bayikayıt.html",context)

def bayisatis(request):
    return render(request,"bayi/bayisatis.html",{})

def siparisEt(request):
       
    context = {}
    return render(request, 'bayi/bayisiparis.html',context)

def satışSil(request,id):
    satis= Satış.objects.get(pk=id)
    satis.delete()
    return redirect("bayi")

def bayiBakim(request):
    
    context = {}
    return render(request, 'bayi/bayiBakim.html',context)

def bakimSil(request,id):
    bakim = Bakım.objects.get(pk=id)
    bakim.delete()
    return redirect("bayi")

def siparişSil(request,id):
    firmaSiparis= Sipariş.objects.get(pk=id)
    firmaSiparis.delete()
    return redirect("bayi")

def send_email(bayi,siparişler):
    subject = "Bir siparişiniz var."

    message = """
    Merhaba firma yöneticisi,

        {} bayisi tarafından aşağıdaki listelenen ürünler sipariş edilmiştir.
    """.format(bayi)
    for sipariş in siparişler:
        message+="""
        ürün adı:   {}
        ürün adeti: {} 
        
    """.format(sipariş.ürün, sipariş.adet)+"-"*50
    from_email = "sanbaysat@gmail.com"
    admin_mail = User.objects.all()[0].email
    if subject and message and from_email:
        try:
            send_mail(subject, message,from_email,[admin_mail])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')