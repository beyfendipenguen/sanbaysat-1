from django import forms
from django.forms import ModelForm
from core.models import  Sipariş_Ürün, Bayi, Satış, Müşteri, Bakım

class nameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=100)

class siparişÜrünForm(ModelForm):
    class Meta:
        model = Sipariş_Ürün
        fields= ['ürün','adet']

class bakımYapForm(ModelForm):
    class Meta:
        model = Bakım
        fields = ['açıklama','tutar']

class SiparisForm(ModelForm):
    class Meta: 
       model = Sipariş_Ürün
       fields = '__all__'


class satışEkleForm(ModelForm):
    class Meta: 
       model = Satış
       fields = ['müşteri','ürün','satış_fiyatı','alış_fiyatı','ödeme_aracı']

class müşteriEkleForm(ModelForm):
    class Meta: 
       model = Müşteri
       fields = ['adı','soyadı','adres','telefon']


class createBayi(ModelForm):
    class Meta:
        model = Bayi
        fields = ['adı','şehir','telefon','adres','ülke']
    