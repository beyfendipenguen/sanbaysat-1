from django.forms import ModelForm
from core.models import Ürün, Ödeme, Reçete, Hammadde
from django import forms
"""
class modelAdıEkleForm(ModelForm):
    class Meta:
        model = modelAdı
        fields = "__all__"
"""
class reçeteGüncelleForm(ModelForm):
    class Meta:
        model = Reçete
        fields = ['ürün','hammadde','miktar']

class hammaddeGüncelleForm(ModelForm):
    class Meta:
        model = Hammadde
        fields = ['adı','depodaki_miktar','tedarik_süresi','kritik_seviye']

class reçeteEkleForm(ModelForm):
    class Meta:
        model = Reçete
        fields = "__all__"
    
class hammaddeEkleForm(ModelForm):
    class Meta:
        model = Hammadde
        fields = "__all__"



class ürünGüncelleForm(ModelForm):
    class Meta:
        model = Ürün
        fields = ['adı','kapak','genişlik','yükseklik','kapasite','voltaj','ağırlık','bakım_aralığı','fiyat']


class ürünEkleForm(ModelForm):
    class Meta:
        model = Ürün
        fields = "__all__"


class ödemeEkleForm(ModelForm):
    class Meta:
        model = Ödeme
        fields = "__all__"