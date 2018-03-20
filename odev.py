#1. soru
def ciroHesapla(tSM,hM,bOG,sG,sAHG):
    kDCiro=tSM-(hM+bOG+sG+sAHG)
    return kDCiro

toplamSatis=int(input("Toplam satış miktarı:"))
hMaliyeti=int(input("Hammadde maliyeti:"))
bOGider=int(input("Bakım onarım giderleri:"))
sGider=int(input("Sevkiyat giderleri:"))
sAHizmetGiderleri=int(input("Satın alınan hizmet giderleri:"))

sonuc=ciroHesapla(toplamSatis,hMaliyeti,bOGider,sGider,sAHizmetGiderleri)

if (sonuc>=1000):
    print("Katma değer cironuz yüksek",sonuc,"tl")
elif (500<=sonuc<=999):
    print("Katma değer cironuz normal",sonuc,"tl")
else:
    print("Katma değer cironuz düşük",sonuc,"tl")
    

#2.soru
def mCalismaSureHesabi(calismaSuresi,toplamMusteriSayisi):
    musteriCalismaSuresi=calismaSuresi/toplamMusteriSayisi
    return musteriCalismaSuresi

birinciYil=mCalismaSureHesabi(170,50)
ikinciYil=mCalismaSureHesabi(220,70)

print(birinciYil)
print(ikinciYil)
print("İki yıl arasındaki fark:",round(ikinciYil-birinciYil,2))
#3.soru
def ilkAltiFonks(yazilimGeliri,finGeliri,uSatisGeliri,calisanMaas,kiraGideri,donMaliyeti):
    ilkAltiKar=(yazilimGeliri+finGeliri+uSatisGeliri)-(calisanMaas+kiraGideri+donMaliyeti)
    return ilkAltiKar

print("İlk altı ay için gelir-giderler")
a=int(input("Yazılım geliriniz:"))
b=int(input("Finansman geliriniz:"))
c=int(input("Ürün satış geliriniz:"))
d=int(input("Çalışan maaşlarınız:"))
e=int(input("Kira giderleriniz:"))
f=int(input("Donanım maliyetiniz:"))

ilkAltiAy=ilkAltiFonks(a,b,c,d,e,f)

print("İlk 6 aydaki kârınız",ilkAltiAy,"tl")

def sonAltiFonks(yazilimGelir,spGeliri,eTicaretG,urunSatisG,calisanM,kiraGideri,bakimM):
    sonAltiKar=(yazilimGelir+spGeliri+eTicaretG+urunSatisG)-(calisanM+kiraGideri+bakimM)
    return sonAltiKar

print("Son altı ay için gelir-giderler")
x=int(input("Yazılım geliriniz:"))
y=int(input("Sponsorluk geliriniz:"))
z=int(input("E-ticaret geliriniz:"))
t=int(input("Ürün satış geliriniz:"))
m=int(input("Çalışan maaşlarınız:"))
n=int(input("Kira giderleriniz:"))
p=int(input("Bakım maliyetiniz:"))

sonAltiAy=sonAltiFonks(x,y,z,t,m,n,p)

print("Son 6 aydaki kârınız",sonAltiAy,"tl")


if (sonAltiAy-ilkAltiAy>=5000):
    print("İşletme çok kârlı")
elif(1000<=sonAltiAy-ilkAltiAy<=5000):
    print("İşletme kârı normal")
else:
    print("İşletme yeterince kârda değil")

#4.soru
def ortStokHesapla(dBasiStok,dSonuStok):
    ortStok=(dBasiStok+dSonuStok)/2
    return ortStok

koltuk=int(input("Dönembaşı koltuk stoğunuz:"))
yatak=int(input("Dönembaşı yatak stoğunuz:"))
dolap=int(input("Dönembaşı dolap stoğunuz:"))

genelStok=ortStokHesapla(koltuk+yatak+dolap,(koltuk-25+10)+(yatak-20+15)+(dolap-10+5))

print("Ortalama stoğunuz",genelStok)

