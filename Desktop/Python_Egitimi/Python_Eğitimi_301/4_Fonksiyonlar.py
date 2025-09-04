#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 14:06:19 2025

@author: mumineaisedemiral
"""

#Fonksşyonların en önemli amacı aynı kodların tekrar tekrar yazılmasını önlemektir.
# defination(tanımlama)

def seslen():
    print("Sesleniyorum!!")
    print("Naber!!")
    print("Nasılsın!!")
    print("Seslenmeyi bitirdim!!")

seslen()  # call - çağırma
seslen()  # invoke
seslen()
seslen()
seslen()
seslen()
print(type(seslen))
print(seslen) # depolanma adresini yazdırır.

#%% PARAMETRESİZ FONKSIYONLARA GİRİŞ
def isimSoyle():
    print("Mümine Aişe Demiral")

def bilgileriSoyle():
    isimSoyle()          # fonksiyon içersinde fonksiyon kullanabiliriz
    print("Bolu Abant İzzet Baysal Üniversitesi")
    print("Bilgisayar Mühendisi")
    print("Darıca/Kocaeli")
    
bilgileriSoyle() # parantez koyarak çağırmış oluruz
bilgileriSoyle()
bilgileriSoyle()
bilgileriSoyle()
bilgileriSoyle()

for i in range(10):
    isimSoyle()
#%% PARAMETRELİ FONKSİYONLARA GİRİŞ

def bilgiVer():
    print("Mümine Aişe Demiral")

#Parametreli
def toplama(sayi1,sayi2):
    print("{}+{}={} ".format(sayi1, sayi2,sayi1+sayi2))

#argümanlar
toplama(11, 25)
toplama(19,27)

def isimSoyle(isim):
    print( "Kullanıcı Bilgisi:",isim)
isimSoyle("Hafsa Demiral")
isimSoyle("Halime Demiral")
isimSoyle("Şemseddin Demiral")
isimSoyle("Sultan Unutur ")



#%% RETURN

def bilgiVer():
    print("Mümine Aişe Demiral")

bilgiVer()

#overriding - geçersiz kılmak
def bilgiVer(isim):
    print(isim)
    return isim + " kişiyle alakalı bilgi verildi"
    
bilgiVer("Hafsa Demiral")

sayi=10
print(sayi)
sayi=20
print(sayi)

urun = bilgiVer("Ayca Kapı")
print(urun)


def carp(sayi1,sayi2):
    return sayi1*sayi2
print(45)
print(carp(5, 9)

def topla(sayi1,sayi2):
    return sayi1+sayi2

topla(75, 21)

#%% RETURN DEĞERİ ÖRNEĞİ

def mutlakDegerliCarpim(sayi1,sayi2):
    return abs(sayi1*sayi2)

print(mutlakDegerliCarpim(-5, -6)*3)
print(mutlakDegerliCarpim(5, -6)/5)
print(mutlakDegerliCarpim(5, 6))

def uckeninKenarlarınıSoyle(k1,k2,k3):
    return "Kenar1: {}".format(k1),"Kenar2:{} ".format(k2),"Kenar3:{}".format(k3)

print(uckeninKenarlarınıSoyle(3, 4, 5))
bilgi1,bilgi2,bilgi3=uckeninKenarlarınıSoyle(3,4,5)
print(bilgi1)
print(bilgi2)
print(bilgi3)


from math import pi

def daireAlanCevre(r):
    return[pi * r *r,2*pi*r]

def daireninAlanVeCevreBilgiVer(cevreVeAlan):
    print("Dairenin Alanı:",cevreVeAlan[0])
    print("Dairenin Çevre:",cevreVeAlan[1])

print(daireAlanCevre(5))
daireninAlanVeCevreBilgiVer(daireAlanCevre(5))


#%% PASS BY VALUE  ///  PASS BY REFERENCE

#Pass By Value (Değer Geçişi)
#Pass By Reference (Adres Geçişi)

sayi1=10
sayi2=sayi1
print(sayi1,sayi2)
sayi1 = 20
print(sayi1,sayi2)


liste1 = [10,20,30]
liste2 = liste1   # değerlerindense adreslerinin eşitlenmesidir.
print(liste1,liste2) # adresleri eşitlendiği içinde liste 1 de yapılan değişiklik liste 2 yide etkileyecektir.
liste1[0]=75
print(liste1,liste2)



# PASS BY VALUE
def guncelle(sayi):
    print("sayi id:",id(sayi))
    sayi=9
    print("sayi id", id(sayi))
    print("Func Sayi",sayi)
    
sayimiz=20
print("sayimiz id",id(sayimiz))
print("sayimiz değer",sayimiz)
guncelle(sayimiz)
print("güncellendikten sonra sayimizin değeri:",sayimiz)



def listeGuncelle(liste):
    print("Liste id :",id(liste))
    liste[0]=1000
    print("Liste id: ",id(liste))
    
listemiz=[0,10,20,30]
listeGuncelle(listemiz)
print(listemiz)
          


#%% TYPES OF ARGUMENTS

#Types of Arguments(Argüman Tipleri)
#positional,keyword,default,variable length


def topla(s1,s2=0):
    print("s1: {} s2:{}".format(s1, s2))
    return s1+s2
print(topla(10, 20)) # MUHAKKAK VERİLMESİ GEREKEN DEĞERLERE POSITIONAL ARGUMENT DENİR.
print(topla(50))     # DEFAULT ARGUMAN DENİR

print(topla(s2=150,s1=100)) # vermiş olduğumuz sıraya göre değil keyworde göre argüman sıralanması keyword argumandır.


def topla(*args,**kwargs): # * ismi olmayan argumanları ** ismi olan argumanların tutulmasını sağlar.
    print(args)
    print(kwargs)
    if kwargs["islem"] =="+":
        print("Yapılan işlem toplama işlemidir!!!")
        print(sum(args))
    else:
        print("Bu fonksiyon toplama işlemini desteklememektedir")
    
topla(2,3,4,5,6,7,8,9,10,75,95,islem="+")

#%% POSITIONAL ARGUMENTS

def hesapla(s1,s2,islem):
    sonuc = None
    if islem == "+":
        sonuc = s1 + s2
    elif islem == "-":
        sonuc= s1-s2
    elif islem =="*":
        sonuc= s1*s2
    elif islem == "/":
        sonuc= s1/s2
    elif islem == "%":
        sonuc= s1%s2
    else:
        sonuc= "5 temel işlem dışında hesaplama yapılmamaktadır!!"
        return sonuc

print(hesapla(75,15,"+"))
print(hesapla(75,15,"-"))
print(hesapla(75,15,"*"))
print(hesapla(75,15,"/"))
print(hesapla(75,15,"%"))
print(hesapla(75,15,"//"))


#%% KEYWORD AND DEFAULT ARGUMENTS

def ogrenciBilgiSoyle(isim,numara,adres="",sube=""):
    print("Öğrencinin ismini : ",isim)
    print("Öğrencinin numarası : ",numara)
    if adres !="":
        print("Öğrencinin adresi : ",adres)
    if sube !="":
        print("Öğrencinin subesi : ",sube)

ogrenciBilgiSoyle("Mümine", 197, "Kocaeli", "A")
ogrenciBilgiSoyle("Sude", 198,sube= "A")

#%% VARIABLE - LENGTH ARGUMENTS
# * keywordu olmayan argümanları tutar. (*args)
# ** ise keywordu olan argümannları tutar. (**kwargs)

def bilgileriGoster(isim,*args,fatih="",**kwargs):
    print("positional Argument",isim)
    print("positional Argument",fatih)
    print(args)
    print(kwargs)
    
bilgileriGoster("Fatih","Kaan","Aysel",
                fatih=26, kaan = 29,aysel =36)


#%%
from math import sqrt
def karekokHesapla(*args):
    liste=[]
    for sayi in args:
       # print(round(sqrt(sayi),4))
       liste.append(round(sqrt(sayi),4))
    return liste

karekokHesapla(5,7,9,16,25,34)


#%%  LOCAL VE GLOBAL KAVRAMI

sayi = 10  # global değişken

def func1():
    sayi2 = 20  # yerel değğişken

def func2():
    global sayi
    sayi=20
    print("Local sayi:",sayi,"Adres:",id(sayi))

print("Global sayi:",sayi,"Adres:",id(sayi))
func2()
print("Global sayi:",sayi,"Adres:",id(sayi))



if True:
    y=50
print(y)

while True:
    z = 100
    break
print(z)

isim = "Fatih"

print(globals()) # programdaki bütün global değişkenleri yazdırır.

print(globals()["isim"])


#%%  RECURSIVE VE ITERATIVE FONKSIYONLAR

#fonksiyonun kendi kendini çağırmasına recursive kendini tekrarlamasına ise iterative fonksiyon denir

def iterFunc():  # tekrarlanma usulü
    for i in range(sayi,-1,-1):
        print(i)
iterFunc(20)



def recFunc(sayi):  # kendi kendini çağırması usulü
    if sayi == -1:
        return None
    print(sayi)
    recFunc(sayi-1)
recFunc(20)

#%% faktöriyel fonksiyonunu hem itterative hem de recusive şeklinde kullanımı

def itterFact(n):
    if n>=0:
        sonuc = 1
        for i in range(2,n+1):
            sonuc *=i
            return sonuc
    else:
        return("Lütfen doğal sayı giriniz")
print(itterFact(5))
print(itterFact(6))
print(itterFact(-1))



def recFact(n):
    if type(n) == int and n>=0:
        if n ==0:
            return 1
        return n *recFact(n-1)
    else:
      return "Lütfen doğal sayı giriniz"  

print(recFact(5))
print(recFact(6))
print(recFact(-1))


#%%  LAMBDA ANONYMOUS FUCTION (İSİMLERİ OLMAYAN FONKSİYONLAR)

#ram de yer kaplamaz 
# geçici olarak kullanmak istediğimiz fonksiyonları lambda olarak yazarız

def kareAl(sayi):
    return sayi * sayi

print(type(kareAl))
print(kareAl(5))

lambdaKareAl = lambda sayi : sayi * sayi # ilk sayi parametresi ikinci kısım return değeri olur
print(type(lambdaKareAl))
print(lambdaKareAl(5))

lambdaTopla = lambda sayi1,sayi2:sayi1 +sayi2
print(lambdaTopla(10.2,17.7))

fullName = lambda name,surname:name+" "+surname

print(fullName("mümine aişe","demiral"))



kareAlFonk = kareAl
print(kareAlFonk(15))



kupAl = lambda sayi : sayi*sayi*sayi
kupAl2 =lambda s: s**3

print(kupAl(3))
print(kupAl2(6))



tersYaz =lambda string:string[::-1]
print(tersYaz("Mümine"))



#%% ÖZEL FONKSİYONLAR filter() map() reduce()


sayilar = [3,2,5,6,-7,14,4,-5,-6,-5,-3,11,110,-15]

def pozitifMi(s):
    return s>0

for sayi in sayilar:
    if sayi>0:
        print(sayi)

print(pozitifMi(5))
print(pozitifMi(2))
print(pozitifMi(0))
print(pozitifMi(-3))

pozitifSayilar = list(filter(pozitifMi, sayilar))
pozitifSayilar2 = list(filter(lambda s:s>0, sayilar))
negatifSayilar = list(filter(lambda s:s<0, sayilar))
negatifSayilar2 = [sayi for sayi in sayilar if sayi not in pozitifSayilar]


#%% filter fonk örnek 1
sayilar =[3,2,5,6,-7,14,4,-5,-6,-5,-3,11,110,-15]

ciftSayilar = list(filter(lambda s:s%2==0, sayilar)
tekSayilar = list(filter(lambda s:s%2==1, sayilar)

                 
def ciftMi(s):
    return s%2==0
def tekMi(s):
    return s%2==1


ciftSayilar2 = list(filter(ciftMi, sayilar))
tekSayilar2 = list(filter(tekMi, sayilar)



#%% Map fonksiyonu
#dizi içersindeki değerleri sıralandırmaya yarayan fonksiyondur

def kareAl(s):
    return s **2

sayilarKaresi=[]
for sayi in sayilar:
    print(sayi**2)
    sayilarKaresi.append(sayi**2)

print(sayilarKaresi)




sayilarKaresi2 =list(map(kareAl, sayilar))
sayilarKaresi3 = list(map(lambda s:s*s, sayilar))

print(sayilarKaresi2)
print(sayilarKaresi3)


#%% reduce fonksiyonu
#REDUCE FONKSİYONUNUN OLAYI 2 TANE BİLEŞEN ALMASIDIR.
from functools import reduce

sayilar =[3,4,6,-1,7]

def topla(s1,s2):
    return s1+s2

toplam = reduce(topla,sayilar)
print(toplam)

#%%
# Reduce Fonksiyonu kullanarak çarpma işlemi yapıcaz ve dizideki en büyük
# ve en küçük sayıyı bulmaya çalışıyoruz
from functools import reduce

sayilar = [2,1,6,5,4,8,-2,-4]


def carp (s1,s2):
    return s1*s2
carpimSonucu =reduce(carp, sayilar)

def enBuyuk(s1,s2):
    if s1>s2:
        return s1
    else:
        return s2
enBuyukSayi = reduce(enBuyukSayi, sayilar)
print(max(sayilar),enBuyukSayi)

#%% ZİP FONKSİYONU
#bilgilerin değerlerin sıkıştırılmasını sağlayan fonksiyondur.

numaralar = [1,2,3,4,5,6]
isimler = ["Kaan","Arzu","Dilek","Kemal","Mehmet"]

ziplenmiş = zip(numaralar,isimler)

bilgiler = list(ziplenmiş)

yaslar = (15,8,19,32,45)


bilgiler = list(zip(numaralar,isimler,yaslar))



for no,ad,yas in bilgiler:
    print("No: {} Adı: {} Yaşı: {}".format(no ,ad ,yas))


ziplenmiş = zip(numaralar,isimler)
print(list(ziplenmiş))     # tuple halde 

ziplenmiş = zip(numaralar,isimler)
bilgiler = dict(ziplenmiş) # key value şeklinde açılmış.
print(bilgiler)


# EN AZ ELEMAN VARSA ONU ZİPLER.


#%% MAP  VE REDUCE ÖRNEK
from functools import reduce

katSayilar = [0.2,0.3,0.5]
notlar = [60,40,70]

donemSonuNotlar1 = []

for i in range(3):
    donemSonuNotlar1.append(katSayilar[i]*notlar[i])
    
print(donemSonuNotlar1)
    

donemSonuNotlari2 = list(map(lambda s1,s2:s1*s2, katSayilar,notlar))

donemSonuNotu = reduce(lambda s1,s2:s1+s2,donemSonuNotlari2)

#%% enumerate , all , any

sayilar = (20,30,40,50,111)

count=1
for sayi in sayilar:
    print("{}.sayı ={}".format(count, sayi))
    count +=1

print(list(enumerate(sayilar)))

for no,sayi in enumerate(sayilar,1):
    print("{}.sayı ={}".format(no, sayi))



#all() # bütün değerler true ise return true olur
#any() # en az 1 tanesi true ise return true olur


#tamamı true mu ?
print(all([True,True,True]))
print(all([True,False,True]))

#Herhangi bir tanesi True mu?
print(any([True,True,True]))
print(any([True,False,True]))
print(any([False,False,False]))


#%% bir fonksiyonun fonksiyon return etmesi

def bilgiVer(func):
    print("Bilgi veriliyor...")
    return func
    

def kullanıcıBilgisiVer(isim):
    return "Adı: "+isim
bilgiVer(kullanıcıBilgisiVer)("Mümine Aişe")

print(bilgiVer(kullanıcıBilgisiVer)("Mümine Aişe")
)



#%% DECORATORS (SÜSLEMELER)

def funcInfo(func):
    #inner function
    def bilgiVer():
        print("Fonksiyonun çalışması başladı!")
        func()
        print("Fonksiyonun çalışması bitti")
    return bilgiVer

@funcInfo     # bir fonksiyonun çalışmasından önce başka bir fonksiyon çalışmasını istiyorsan bu decoratifi kullanılır.
def soruSor():
    print("Soru Sordum!!")
@funcInfo 
def cevapVer():
    print("Cevap Verdim!!")
    
#funcInfo(soruSor)()
soruSor()
cevapVer()
#funcInfo(cevapVer)()


#%%
def funcInfo(func):
    def inner(*args,**kwargs):            # *ARGS  Fonksiyona birden fazla sayıda pozisyonel argüman (yani sıra ile verilen değerler) göndermemizi sağlar.
        print("Konuşmaya Başladı!!")      # **KWARGS Fonksiyona birden fazla anahtar-değer çifti göndermemizi sağlar. 
        func(*args,**kwargs)
        print("Konuşmayı Bitirdi!!")
    return inner
@funcInfo
def soruSor(isim, yas, soru):
    print("soru soran kişinin bilgileri: ")
    print("Soru soran kişinin adı: {}".format(isim))
    print("Sorusu : {}".format(soru))
    try:
        print(kwargs["bilgi"])
    except Exception:
        print("Elimizde bir bilgi bulunmamaktadır.")
@funcInfo
def cevapVer(isim, yas, soru):
    print("Cevap veren kişinin bilgileri: ")
    print("Cevap veren kişinin adı: {}".format(isim))
    print("Cevabı : {}".format(soru))
#funcInfo(soruSor)("Mümine",20,"nasılsın?")
#funcInfo(cevapVer("Kaan", 23, "İyiyim"))
    

soruSor("Mümine",20,"nasılsın?")
cevapVer("Kaan", 23, "İyiyim")




#%%  DEKORATÖRLER ÖRNEK 1
# Liste içindeki sayıların karesi ve karekökünü hesaplama
# Programın çalışma süresini hesaplama

from math import sqrt
import time

# 1 Ocak 1970

def calismaSuresiniHesapla(func):
    def inner(*args,**kwargs):
        baslangic = time.time()
        func(*args,**kwargs)
        bitis = time.time()
        print("Fonksiyonun çalışma süresi:",bitis-baslangic)
    return inner  
@calismaSuresiniHesapla
def karekokAl(sayilar):
    sayilar = [sqrt(sayi) for sayi in sayilar]
    return sayilar
@calismaSuresiniHesapla
def kareAl(sayilar):
    sayilar = [sayi ** 2 for sayi in sayilar]
    return sayilar





sayilar =list(range(10000))

#print(calismaSuresiniHesapla(karekokAl)(sayilar))

#print(calismaSuresiniHesapla(kareAl)(sayilar))

karekokAl(sayilar)
kareAl(sayilar)






























