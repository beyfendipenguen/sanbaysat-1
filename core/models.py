from django.db import models
from django.contrib.auth.models import User

# Create your models here.
durumlar= [
    ('o','onaylandı'),
    ('b','beklemede'),
    ('r','reddedildi')
]

onaylanan_durumlar = [
    ('h','hazırlanıyor'),
    ('y','yola çıktı'),
    ('t','teslim edildi')
]


dürümler=[
    (True,'Onaylandı'),
    (False,'Onay Aşamasında')
]


kapaklar = [
    ('ALM','Aliminyum'),
    ('STL','Çelik')
]

voltajlar = [
    (12,12),
    (24,24)
]

ödeme_araçları = [
    ('Kredi','Kredi kartı'),
    ('Nakit','Nakit ödeme')
]


class Bayi(models.Model):
    adı = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    şehir = models.CharField(max_length=20)
    telefon = models.CharField(max_length=11)
    adres = models.TextField()
    ülke = models.CharField(max_length=20)
    aktif = models.BooleanField(default=False)

    def __str__(self):
        return self.adı


class Müşteri(models.Model):
    bayi = models.ForeignKey(Bayi,on_delete=models.CASCADE) 
    adı = models.CharField(max_length=20)
    soyadı = models.CharField(max_length=20)
    adres = models.TextField()
    telefon = models.CharField(max_length=11)

    def __str__(self):
        return str(self.adı)


class Hammadde(models.Model):
    adı = models.CharField(max_length=20)
    depodaki_miktar = models.IntegerField(default=0)
    tedarik_süresi = models.IntegerField(default=1)
    kritik_seviye = models.IntegerField(default=0)
    
    def __str__(self):
        return self.adı



class Ürün(models.Model):
    adı = models.CharField(max_length=20)
    kapak = models.CharField(max_length=3, choices=kapaklar, default='ALM')
    genişlik = models.IntegerField()
    yükseklik = models.IntegerField()
    kapasite = models.IntegerField()
    voltaj = models.IntegerField(choices=voltajlar)
    ağırlık = models.IntegerField()
    bakım_aralığı = models.IntegerField()
    fiyat = models.FloatField()

    
    #depodaki_miktar= models.IntegerField(default=0)
    # Depodaki miktar ürün üretmek için eklendi,
    
    def __str__(self):
        return self.adı



class Reçete(models.Model):
    ürün = models.ForeignKey(Ürün,on_delete=models.DO_NOTHING)
    hammadde = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING)
    miktar = models.IntegerField(default=0)


class Sipariş(models.Model):
    bayi = models.ForeignKey(Bayi, on_delete=models.DO_NOTHING)
    sipariş_tarihi = models.DateField(auto_now_add=True,editable=False,blank=True)
    teslim_tarihi = models.DateField(null=True, editable=True,blank=True)
    tutar = models.FloatField(null=True,blank=True)
    durum= models.CharField(null=True, choices=durumlar,max_length=13,default='b')
    sipariş_takibi = models.CharField(null=True, choices=onaylanan_durumlar,max_length=13,default='h')

    def __str__(self):
        return str(self.pk)


class Sipariş_Ürün(models.Model):
    sipariş = models.ForeignKey(Sipariş, on_delete=models.CASCADE)
    ürün =  models.ForeignKey(Ürün, on_delete=models.CASCADE)
    adet = models.IntegerField(default=1)

class Ödeme(models.Model):
    sipariş = models.ForeignKey(Sipariş, on_delete=models.DO_NOTHING)
    tutar = models.FloatField()
    tarih = models.DateField(auto_now_add=True,editable=False,blank=True)
    ödeme_aracı = models.CharField(max_length=5,choices=ödeme_araçları)


class Satış(models.Model):
    bayi = models.ForeignKey(Bayi, on_delete=models.DO_NOTHING)
    müşteri = models.ForeignKey(Müşteri, on_delete=models.DO_NOTHING)
    ürün = models.ForeignKey(Ürün, on_delete=models.DO_NOTHING)
    tarih = models.DateField(auto_now_add=True,editable=False,blank=True)
    satış_fiyatı = models.FloatField()
    alış_fiyatı = models.FloatField()
    ödeme_aracı = models.CharField(max_length=5,choices=ödeme_araçları)

class Bakım(models.Model):
    satış = models.ForeignKey(Satış, on_delete=models.CASCADE, default=None)
    bakım_tarihi = models.DateField(auto_now_add=True, editable=False, blank=True)
    gelecek_bakım_tarihi = models.DateField(null = True,blank=True, default=None)
    açıklama = models.TextField(default="genel bakım")
    tutar = models.FloatField()
 
class Katolog(models.Model):
    ürün = models.ForeignKey(Ürün, on_delete=models.CASCADE)
    bayi = models.ForeignKey(Bayi, on_delete=models.CASCADE)
    satış_fiyatı = models.FloatField()


#TODO hammadde tedarik sayfası yapılacak.
#TODO Bayi muhasebe tablosu
#TODO RestAPI ile müşteri ürün bakım bilgisi
#TODO 

#TODO settings sayfasına current user bayi nasıl olur bi düşün araştır ???
#TODO session araştır.
#TODO sipariş tamamlanmadan çıkınca ürün eklenme bugı
