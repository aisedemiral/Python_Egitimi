#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 17:38:09 2025

@author: mumineaisedemiral
"""

#=============================================#
# NoneType( None Tipi)                        #
# Numeric(Sayısal) Tiplere Giriş              #
# int,float                                   #
# bool                                        #
# complex (Komplex Sayılar)                   #
#                                             #
# Dizi Halindeki Veri Tiplerine Giriş         #
# List (Liste) Veri Tipi                      #
# Tuple Veri Tipi                             #
# Set Veri Tipi                               #
# String (Karakter Dizisi) Veri Tipi          #
# Range (Aralık)                              #
# Dictionary (Sözlük)                         #
#=============================================#


#%%
#        NONETYPE (NONE TİPİ)
# şu anda hangi tipte olduğunu bilmediğimiz veilerde kullanırız.
sehir=None
print(type(sehir))
sehir="İstanbul"
print(type(sehir))

#%%
#       NUMERİC(SAYISAL) TYPE

# int, float

x = 10
y=int(15)

z=10.7
t=float(17.8)
#tip dönüşümü hatırlatma!!!
x1=float(x)
z1=int(z)
t1=int(t)


# bool

anahtar1=True
anahtar2=False

k1 = 3 < 4

anahtar3 =bool(True)
anahtar4= bool(False)

anahtar5= bool(10)
anahtar6= bool(1.2)
anahtar7= bool(-6)

anahtar8= bool(0.0)
anahtar9= bool(0)

anahtar10= int(True)
anahtar11= int(False)

anahtar12= float(True)
anahtar13= float(False)




# complex(karmaşık sayılar)

ks1 = 2 + 3j
ks2 = complex(4,5) # 4 + 5j

toplam = ks1 + ks2 # 6 + 8j
cıkar = ks1 - ks2 # -2 -2j
carp = ks1 * ks2  # (2+3j)(4+5j)=8 + 10j + 12j +(-15)=-5+22j
bol = ks1 / ks2  


sayi1 = 4.5
sayi2 = 7
ks3 = complex(sayi1,sayi2) # 4.5 + 7j
# ks4 = sayi1 + sayi2(j)  veya  ks4= sayi1 + sayi2*j bu şekildeki karmaşık sayı oluşturamayız


#%% DİZİ HALİNDEKİ VERİ TİPLERİNE GİRİŞ

# Tuple Veri Tipi
#Immutable (Değiştirilemez)
#read-only (Sadece Okunabilir)
#Elemanların sequence number (sıra numarası) vardır.
#tuple()
liste1 = [2,4,7,10]
tuple1 = (7,8,11,-5)

tuple2=tuple("Ahmet")
tuple3=tuple([2,1,8,9,10])
tuple4=tuple([6,1,8,9,11,16,-5,0,2])
tuple5=tuple(["A","H","M","E","T"])
tuple6=tuple(("A","H","M","E","T"))

print(liste1,tuple1)

liste1[0]=14
#tuple[0]=15 HATA VERİR
print(liste1,tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

#%%

#String (Karakter Dizisi) Veri Tipi
#Immutable(Değiştirilemez) "Doğrudan değiştirilemez"
#Elemanların sequance number (sıra numarası) vardır.
#

karakter1 = "F"
karakter2 = 'F'

isim = "Fatih Kaan"
isim = isim[:6] +"Selim"
print(isim)

#%%
#Range Veri Tipi
aralik = range(10) # [0,10] x eleman Z
print(aralik,type(aralik))

listAralik = list(aralik)
tupleAralik = tuple(aralik)
setAralik = set(aralik)

print(*aralik) # içindeki değerlere ulamkak için başına yıldız koyarız.
print(*aralik)
print(list(aralik))
print(tuple(aralik))
print(set(aralik))
print(str(aralik))

print(str(listAralik))

# Range(start,stop,step)
aralik1 = range(18,2,-5)
print(list(aralik1))

aralik2 = range(5,14)
print(list(aralik2))

#%% TUPLE (DEMET) VERİ TİPİ

# Tuple Veri Tipi
#Immutable (Değiştirilemez)
#read-only (Sadece Okunabilir)
#Elemanların sequence number (sıra numarası) vardır.
#tuple()

tup1 = (15,26,17,25)
tup2 = ("Ahmet" , "Methmet")
tup3 = (5+4j ,  "Melih" , 74.6 , 159)
tup4 = tuple([79,125,1748,14.69])


#tup1[0]=174 HATA VERİR

butunTupler=tup1+tup2+tup3+tup4

#*******************************************************
# Tuple Elemanlarına Erişmek

tup5=(15,26,17,25)
liste1=[1,7,9,3,8]
print(tup5[0])
print(tup5[1])
print(tup5[2])
print(tup5[3])

print(tup5[1:])
print(liste1[2:4])

print(tup5[::2])
print(tup5[0:len(tup1):2])
print(tup5[-1::-1])

#********************************************************
#Tuple Metotları
tup=(15,26,17,25,178)
#Count
print(tup.count(26)) # count ile o değerden tuple mizde kaç tane olduğunu öğreniriz.
#Index
print(tup.index(26))# indek ile değerimizin kaçıncı indekste olduğunu(bölümde) öğrenirizz.






#%%   LİST(LİSTE) VETİ TİPİ
# Mutable(Değiştirilebilir)
#Elemanlarının sequence number (sıra numarası) vardır.
# list() []

liste1 =list([1,5,7,8,3])   # cont ile oluşan
liste2 = [6,4,9,7,8,10,-5] # [] ile oluşan

print(liste1)
liste1[3]=100
print(liste1)

print(liste2)
liste2[4]=1000
print(liste2)

#*********************************************************
#LİSTE ELEMANLARINA ERİŞMEK
liste3=[6,4,9,7,8,10,-5]
print(liste3[0])
print(liste3[1])
print(liste3[6])

print(liste3[2:5])#liste3[2] liste3[3] liste3[4] elemanlarını gösterir.

print(liste3[1:5:2]) # 1.indexten 5 inci indexe kadar 2 şer attırarak yazdırır.

print(liste3[6])
print(liste3[len(liste3)-1])

print(liste3[-1])
print(liste3[0])
print(liste3[-7])

print(liste3[-len(liste3)])

print(liste3)
print(liste3[:])
print(liste3[::])
print(liste3[::2])

#***********************************************************
#LİSTELEDE EKLEME, GÜNCELLEME VE SİLME

isimler=["Mümine","Aişe","Hafsa","Halime"]
yaslar=[19,20,23,25]
print(isimler)
isimler = isimler + ["Şemseddin","Sultan"]  #DOLAYLI YOLDAN EKLEMEDİR.
print(isimler)

print(isimler)
isimler[0]="HAKAN" #LİSTEYİ GÜNCELLEMEKTEDİR. 
print(isimler)
print(isimler[1:4])
isimler[1:4]= ["rümeysa","oya","mehmet"] #köşeli parantez vb kullanmak zorunlu değildir.
print(isimler)

del isimler[2] # SİLME İŞLEMİ
print(isimler)

isimler = isimler[:1]+isimler[3:] # aradaki değerleri almayarak dolaylı yoldan silme işlemi yapılmaktadır.
print(isimler)

#******************************************************************
#LİSTE METOTLARI
isimler2=["sude","emre","eda","akif"]
yaslar2=[23,26,42,15]
karisikliste=isimler2+yaslar2

karisikliste.extend({14.7,"selma",None,True,5+7j}) # Listeyi genişletme eleman ekleme
karisikliste+=[True,False,9+7j,"Naber?"]

print(karisikliste.index(9+7j)) # içerisindeki değerin indexsini söyler

karisikliste.append(175) # listenin sonuna elemanı ekler

karisikliste.insert(2, 45) #istediğim indexe istediğim değeri ekler

karisikliste.pop() #listeden eleman çıkartır eğer içinde index değeri eklenmezse listenin sonundaki elemanı çıkarır. index değeri verilirse verilen indexi boşaltır.

karisikliste.extend([100,100,100])
karisikliste.remove(100) # arguman olarak değer bekler ve eklenen değeri siler.Birden fazla aynı değer varsa ilk karşılaştığı değeri siler.

liste0=[2,5,7]
print(liste0)
liste0.reverse()
print(liste0)

liste0 +=[-5,8,4,3,10,-9]
liste0.sort() # küçükten büyüğe doğru sıralamada kullanılır
print(liste0)
#%%     ÇOK BOYUTLU LİSTELER
isimler=["Fatih","Kaan","Selime","Oya"]
yaslar=[35,47,55,32]

bilgiler=[["Fatih",35],["Kaan",47],["Selime",55],["Oya",32]]
print(bilgiler[0])
print(bilgiler[1])
print(bilgiler[2])
print(bilgiler[3])

print(bilgiler[0][0])
print(bilgiler[0][1])


bilgiler=[({185:"Fatih"}),("İstanbul","denizli")]
print(bilgiler[0])
print(bilgiler[0][185])
print(bilgiler[1][0])
print(bilgiler[1][1])

#%%    SET (BENZERSİZ) VERİ TİPİ
#Mutable(Değiştirilebilir)
#Elemanların sequance Number(Sıra Numarası)(index değeri) yoktur.
#İçerisinde aynı değerde elemanlar barındırmaz
#{}

set1={5,12,2,6,5,12,2} # aynı elemanları yazdırmaz
print(set1)
set1.remove(12) # silme işlemini metotla yaparız.

set2 = set([5,4,7,8,9,4,7])
print(set2)

#***************************************************
#    SETLERDE ELEMAN EKLEME VE ELEMAN SŞLME İŞLEMİ

set2={4,1,8,9,-5,0,91}
print(set2)

set2.add(150)
print(set2)

set2.clear() #set in içindeki tüm elemanları siler.
print(set2)
set2.update({4,1,8,9,-5,0,91})
print(set2)


print(set2.pop()) # Random bir eleman siler.


set2.remove(-5)
print(set2)

#setlerin içerisinde olmayan bir değeri silmeye çalışırsanız keyerror verir yani setlerin içindeki her değer anahtar olarak tutulur.

#*********************************************************
#       SET METOTLARI
setA={4,1,8,9,-5,0,91,"Kaan","Selim"}
setB={3,4,8,7,-6,14,51,66,78,"MElek","Kaan"}
setC={3,4,8}
setD={100,200,300}

setE=setA # birinden bi objeyi silersek diğerinden de silinir fakat copy ile oluşturursak o zaman silinmez.
#setE=setA.copy()

print(setA)
print(setE)
setA.remove(8)

print(setA.difference(setB))

setA.difference_update(setB) # yukarıda bulduğumuz farklılıkları setA ya ekler.

print(setA.discard(4))  # 4 elemanını siler .doğrudan da kullanabiliriz setA.discard()

print(setA.intersection(setC)) # ikisinin kesişimini bize getirir.
setA.intersection_update(setB)
print(setA)


print(setC.isdisjoint(setD)) # kesişim kümesi boş mu 

print(setC.issubset(setB)) # setD setC nin alt kümesi mi
print(setB.issuperset(setC)) #setC setB yi kapsıyor mu


setA.pop()# kümeden keyfi olarak bir elemanı siler


#%%  Dıctıonary (Sözlük) Veri Tipi

# Mutable (Değiştirilebilir)
# Elemanların sequence nuber (sıra numarası) yerine "KEY" vardır.
# dict() {}

set1 = {"Fatih","Kaan","Aliye"}
sozluk ={1:"Fatih",2:"Kaan",5:"Aliye"}

print(sozluk[5])
print(sozluk.get(2))

#print(sozluk[3])
print(sozluk.get(3,"bu anahtar sözlükte bulunmamaktadır."))
print(sozluk.get(2,"bu anahtar sözlükte bulunmamaktadır."))# var olan bir şeyi önce kullanınca yanlızca o kelimeyi yazdırıyor.

#**********************************************

set1 = {"Fatih","Kaan","Aliye"}
sozluk ={1:"Fatih",2:"Kaan",5:"Aliye"}

print(sozluk[5])
print(sozluk.get(2))


bosSozluk1 = {}
bosSozluk2 = dict()

anahtarlar = [1,2,3]
degerler = ["A","B","C"]
sozluk2Elemanları = zip(anahtarlar,degerler)
#print(*sozluk2Elemanları)

sozluk1=dict(sozluk2Elemanları)
sozluk2=dict([(1,"A"),(2,"B"),(3,"C")])

print(sozluk1)
print(sozluk2)

#********************************************************
#  SÖZLÜKLERDE SEÇME, EKLEME, GÜNCELLEME VEE SİLME

keys = ("mehmet","ali","ahmet")
values = ['Bilgisayar Mühendisi',
          'Makine Mühendisi',
          'Elektronik Mühendisi'
          ]
sozlukElemanlari2 = zip(keys,values)
#print(*sozlukElemanlari2)

bilgiler= dict(sozlukElemanlari2)
print(bilgiler)
print(bilgiler["ali"])

#Sözlükte anahtar değeri yoksa o zaman ekler.
bilgiler["Hasan"] ="Makine Mühendisi"
print(bilgiler)

#Güncelleme
bilgiler["Mehmet"]="Doktor"
print(bilgiler)

#silme 
del bilgiler["ali"]
print(bilgiler)

#*******************************************************
# SÖZLÜK METOTLARI

ogrencilerDers = {'Okan': 'Makine Öğrenmesi',
                  'Armağan':{'Bilgisayar Ağları','Doğal Dil İşleme'},
                  'Kaan':{'Makine Öğrenmesi','Doğal Dil İşleme'},
                  'Fatih':[{'Ders Adı':'Veri Tabanı','Hoca':'Gülşah'},
                           {'Ders Adı':'Doğal Dil İşleme',
                            'Hoca':'Burak'}]}


print(ogrencilerDers["Okan"])
print(ogrencilerDers["Fatih"][0])
print(ogrencilerDers["Fatih"][1])
print(ogrencilerDers["Fatih"][0]['Ders Adı'])

baskaSozluk=ogrencilerDers.copy()
baskaSozluk['Okan']='Matematik'

sozluk1 = dict.fromkeys(["Ali","Ahmet","Aslı"],0)
print(sozluk1)

print(ogrencilerDers.get('Okan'))
print(sozluk1.get('Okan','Bu anahtara sahip bir değer bulunamamaktadır.'))

print(ogrencilerDers.items()) # bütün elemanlar tuples şeklinde bastırılır.
print(ogrencilerDers.keys())  #Anahtar değerleri bastırır.
print(ogrencilerDers.values()) # değerleri bastırır.

# Pop ile verilern elemanı çıkarırız.
print(ogrencilerDers)
ogrencilerDers.pop("Armağan")
print(30*'-')
print(ogrencilerDers)

ogrencilerDers.popitem()#lılo metoduna göre çıkarma işlemi yapar yani son elemanı çıkartır.












