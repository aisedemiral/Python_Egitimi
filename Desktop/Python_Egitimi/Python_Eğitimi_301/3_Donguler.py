#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 17:40:00 2025

@author: mumineaisedemiral
"""
#%%       DÖNGÜLER
print("Mümine Aişe Demiral")
print("Mümine Aişe Demiral")
print("Mümine Aişe Demiral")
print("Mümine Aişe Demiral")
print("*********************************")
#0,1,2,3
for i in range(4):
    print("{} . yazı.Mümine Aişe Demiral".format(i+1))
    
    
#%%    FOR DÖNGÜSÜ
# başlangıç değeri
# bitiş değeri
# adım değeri 

for sayi in range(5,10):#5 6 7 8 9 
    print(sayi)
    
#-------------------------------------
    
isimler=["ahmet","ahu","mehmet","hasan","ayşe","ssude"]

for isim in isimler:
    print(isim)
    
#-------------------------------------

tup= (5.0,"ahmet",{12:"Kemal"})
for eleman in tup:
    print(eleman)
    
#%%   FOR İÇİN ÖRNEKLER
for karakter in "mümine aişe demiral":
    print(karakter)

sayilar=[2,4,6,7,5,3]
for sayi in sayilar:
    print(sayi)
    
karisik=['F',75.8,"Kaan",74,True]
for eleman in karisik:
    print(eleman)
 
bilgiler={"fatih":"Bilgisayar Mühendisi",
          "Kaan":"Kimya Mühendisi",
          "Aliye":"Matematik Mühendisi"}
for key in bilgiler:            #SÖZLÜKTEKİ ANAHTARLARI BİZE ÇIKTI OLARAK VERİYOR.
    print(key)

for key in bilgiler.keys():            #SÖZLÜKTEKİ ANAHTARLARI BİZE ÇIKTI OLARAK VERİYOR.
    print(key)

for key in bilgiler.values():            #SÖZLÜKTEKİ DEĞERLERİ BİZE ÇIKTI OLARAK VERİYOR.
    print(key)

print(bilgiler.items())
for eleman in bilgiler.items():
    print(eleman)

print(bilgiler.items())

for key,value in bilgiler.items(): # tuple halinde yani paket halindeki değerleri açar
    print("Adı: ",key,"Mesleği: ",value)

benzersizSayilar={2,3,5,4,2,3,4,5,6,7,4,6,8} # set kullandık aynı sayıları kabul etmez.
print(benzersizSayilar)

for sayi in benzersizSayilar:
    print(sayi)
    

tupleListesi=[(21,51),(41,54),(-5,4),(-5,-9)]
    
for ikili in tupleListesi:
    sayi1,sayi2=ikili
    print(ikili)
    print(sayi1*4,sayi2*4)

for sayi1,sayi2 in tupleListesi:
    print(sayi1*4,sayi2*4)


tupleListesii=[("Okan",28,1578),("Melike",35,957)]

for ad,yas,siralama in tupleListesii:
    print("Oyuncunun bilgileri:")
    print("Adı: ",ad)
    print("yaşı:",yas)
    print("sıralaması:",siralama)


#%% ÖRNEK 1

Sayilar=[2,3,4,5,1,6,7,61,23,65,87]
tekSayilar=[]
ciftSayilar=list()
for i in Sayilar:
    if i%2==0:
        ciftSayilar.append(i)
    else:
        tekSayilar.append(i)
        
print("Tek sayılar bunlardur {} ve {} kadar tek sayı bulunmaktadır".format(tekSayilar,len(tekSayilar)))
print("Çift sayılar bunlardur {} ve {} kadar çift sayı bulunmaktadır".format(ciftSayilar,len(ciftSayilar)))

#%% ÖRNEK 2
"""
1x1=1. . . . . 10x1=10
1x2=2             . 
.                 .
.                 .
.                 .
1x10=10         10x10=100
çıktısını yazan programı yazınız.
"""

for i in range(1,11):
    for j in range(1,11):
        print("{}x{}={}".format(j,i,i*j),end=" ")
    print()


#%%  ÖRNEK 3
# 1 ile 500 arasında karakökü tam sayı olan sayıları yazdıran program

from math import sqrt

for i in range(1,501):
    if int(sqrt(i))**2==i:
        print("Karekök {}={} {} karekökü tam sayı olan bir sayıdır!".format(i,int(sqrt(i)),i))


















    
    
#%%     WHİLE DÖNGÜSÜ
# başlangıç değeri
# bitiş değeri
# adım değeri 
 
#initialisation
#condition
#increment/decrement


i=1 #  initialisation(ilk değer ataması) 

while i<=5: #condition
    print(i)
    i+=1    #increment/decrement
    
#%%     WHİLE DÖNGÜSÜ ÖRNEKLER

sayilar=[10,15,22,33,44,55]
index=0 # İnitialisayion(ilk değer ataması)
while index<len(sayilar): #Condition(şart)
    print(sayilar[index])
    index +=1 #increment
print("döngü bittikten sonra index değeri",index)
print("Tersten yazdırma.")
index=len(sayilar)-1 #initialization
while index >=0:
    print(sayilar[index])
    index -=1 #decrement

#%% ÖRNEK 2
sayi=1
baslangicDegeri=sayi
bitis=50
toplam=0
while sayi <=bitis:
    toplam = toplam +sayi
    sayi+=1
print("[{} - {}] arasındaki tam sayıların toplamı: {}".format(baslangicDegeri, bitis,toplam))
print("[{} - {}] arasındaki tam sayıların toplamı: {}".format(baslangicDegeri, bitis,sum(range(baslangicDegeri,bitis))))

#%%  ÖRNEK 3
# iki sayi arasındaki 5 veya 7 ye bölünebilen sayıları yazdıran program

baslangic=1
i=baslangic
bitis=100
sayi1=5
sayi2=7
sayac=0

while i<=bitis:
    if i % sayi1 == 0 or i % sayi2 == 0 :
        print(i)
        sayac +=1
    i +=1
print("[{}-{}] aralığında {} veya {} sayısına bölünebilen {} tane sayı vardır.".format(baslangic,bitis,sayi1,sayi2,sayac))  

#%% ÖRNEK 4
"""
en 10 
boy 7
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
yukarıdaki şekili çizdiren program yapınız.
"""

i=0
while i<7:
    j=0
    while j<10:
        print("$",end=" ")
        j+=1
    print() #bir alt satıra geçmesini sağlar
    i+=1
    
    
#%%  ÖRNEK 5
# Girilen sayının sayı değerleri toplamını bulan program
# 785 = 7 + 8 + 5 = 20 

sayi = int(input("İstediğiniz bir sayıyı giriniz:"))
orgSayi=sayi
sayiDegerleriToplamı = 0
sayiDegerleri = []

while sayi > 0:
    sayiDegerleriToplamı += sayi % 10
    sayiDegerleri.append(sayi%10)
    sayi//=10
print("{} sayısının basamaklarındaki sayılar".format(orgSayi))
sayiDegerleri.reverse()
print(*sayiDegerleri)
print("{} sayısının sayı değerlerinin toplamı {} ' dir.".format(orgSayi,sayiDegerleriToplamı))
print("{} sayısının sayı değerlerinin toplamı {} ' dir.".format(orgSayi,sum(sayiDegerleri)))

#%% ÖRNEK 6
# faktöriyel hesabı yapan program

n= int(input("Faktöryelini öğrenmek istediğiniz sayıyı giriniz:"))
fak=1
while n>0:
    fak=fak*n
    n -=1
print(fak)

a=int(input("Faktöryelini öğrenmek istediğiniz sayıyı giriniz:"))

if a>= 0:
    b=1
    sonuc = 1
    while b<=a:
        sonuc *=b
        b*=1
    print("{}!={}".format(a,sonuc))
else:
    print("lütfen doğal sayı giriniz!!")





#%% BREAK CONTINUE PASS ANAHTAR KELİMELERİ

#  BREAK
sayi=1000
while True:
    print(sayi)
    if sayi == 10000:
        break
    sayi+=1000
  
print("aaaaaaaaaaaaaaaaaaa")
    
  
count = 0
while True:
    sayi=1
    while True:
        print(sayi)
        if sayi == 5:
            break
        sayi+=1
    count +=1
    if count ==3:
        break
print("aaaaaaaaaaaaaaaaaaa")

#  CONTINUE

for sayi in range(1,50):
    if sayi %5==0:
        continue
    print(sayi)

print("aaaaaaaaaaaaaaaaaaa")

i=0
while i<5:
    if i%2==1:
        i+=1
        continue
    i+=1
    print(i)

# PASS

for sayi in range(1,50):
    pass
print("başka işlemler yapacaağız.")


if i==0:
    pass
else:
    pass



#%% ÖRNEK :bir stringin içerisindeki karakterin indexini bulma

isim = "Mümine Aişe Demiral"
harf="m"
harf=harf.lower()

index=0
for karakter in isim.lower():
    if karakter == harf:
        print("{} harfi {} indexinde bulunmaktadır.".format(harf,index))
    index +=1


print(isim.index(harf)) # ilk bulduğu değeri yazdırır 



#%%  ENUMERATE FONKSİYONU

isim="Beşiktaş"
harf="e"
index =0
for harf in isim:
    print("{} harfi {} . indekste bulunmaktadır".format(harf, index))
    index +=1


print(isim)
print(list(enumerate(isim)))  # isimi alıp 0 dan başlayıp numaralndırmayı sağlar

for index,harf in enumerate(isim):
    print("{} harfi {} . indekste bulunmaktadır".format(harf, index))

for index,harf in enumerate("Mümine aişe demiral ".lower()):
    if harf == "a":
        print("{} harfi {} . indekste bulunmaktadır".format(harf, index))

#%%  ÖRNEKK
# Kullanıcı girişi bilgilerini doğru girdiği taktirde istediği kadar sayı
#girebilmesini ve bunları küçükten büyüğe sıralayabilmesini sağlayan programı
#yazınız.
#Kullanıcı Adı: hesapmakinesi
#Şifre: hesap12345


adi="hesapmakinesi"
sifre="hesap12345"

while True:

    kullanıcıAdi=input("Lütfen kullanıcı adınızı giriniz:")
    kullaniciSifre=input("Lütfen şifrenizi giriniz:")

    if kullanıcıAdi!=adi:
        print("Sistemde böyle bir kullanıcı bulunmamaktadır.")
    elif sifre != kullaniciSifre:
        print("paralonaızı yanlış girdiniz.")
    else:
        sayıAdedi=int(input("Lütfen kaç adet sayı girmek istediğinizi giriniz:"))
        sayilar=[]
        
        for i in range(sayıAdedi):
            sayi=int(input("Lütfen {}.sayıyı giriniz".format(i+1)))
            sayilar.append(sayi)
        sayilar.sort()
        
        for sayi in sayilar:
            print(sayi,end=" ")
        print()
        break
        

#%% ÖRNERK : BANKA ATM

#KArtın bir şifresi vardır.
#Kartın başlangıçta bakiyesi 500 TL'dir.
#3 defa yanlış şifre girilince kart bloke olacaktır.
#ATM'nin işlem menüsünde para öekme,para yatırma,bakiye sorgulama
#ve kart iade işlemi yapılmaktadır.


_kartSifre=1234
_bakiye=500
sifre_sayac=3

login=False
while True:
    if login==False:
        sifre=int(input("Lütfen Şifrenizi giriniz: "))
    if sifre ==_kartSifre:
        login = True
        print("****ATM MENÜSÜ****")
        print("1.Para Çek")
        print("2.Para Yatır")
        print("3.Bakiye Sorgulama ")
        print("4.Kart İade")
        print("******************")
            
        secim=int(input("Hangi işlemi yapmak istiyorsunuz:"))
        if secim ==1:
            miktar =int(input("Kaç TL çekmek istiyorsunuz."))
            if _bakiye<miktar:
                print("Yeterli miktarda bakiyeniz bulunmamaktadır.Ana menüye yönlendiriliyorsunuz.")
                continue
            _bakiye-=miktar
        elif secim ==2:
            miktar =int(input("Kaç TL yatırmak istiyorsunuz."))
            _bakiye=_bakiye+miktar
        elif secim ==3:
            print("Bakiyeniz {} TL'dir.".format(_bakiye))
        elif secim==4:
            print("Yine Bekleriz!")
            break
        else:
            print("Menüde olmayan bir seçi yaptınız. Ana menüye yönlendiriliyorsunuz.")
    else:
        sifre_sayac-=1
        if sifre_sayac<=0:
            print("Kartınız bloke olmuştur!Lütfen bankanız ile iletişime geçiniz.")
            break

#%% FOR - ELSE

sayilar =[3,7,11,20]
for sayi in sayilar:
    if sayi%2==0:
    print("{} çift sayıdır.".format(sayi))
    break # else bloğunun çalışmamasını istiyorsak bizim break komutunu eklememiz gerekmektedir.
else:
    print("çift sayı bulunamamaktadır.")

#%%For döngüsünün etkili kullanıldığı yerler

sayilar=[3,5,7,1,-2,0,11]

sayilarinKareleri=[]
for sayi in sayilar:
    sayilarinKareleri.append(sayi*sayi)
print(sayilarinKareleri)

sayilarinKareleri2=[sayi*sayi for sayi in sayilar]
sayilarinKareleri2Tuple=(sayi*sayi for sayi in sayilar)
print(sayilarinKareleri2)
print(tuple(sayilarinKareleri2Tuple))






















