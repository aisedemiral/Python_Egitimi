#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 20:41:01 2025

@author: mumineaisedemiral
"""

# OOP OBJECT ORIENTED PROGRAMMING (NESNE YÖNELİK PROGRAMLAMA)
#Object Oriented Programming
    #Her şey bir objedir . Hayatta görünen her şey bir objedir
    #Her objenin attribute'leri vardır. (Attribute, Property, Özellikler)(isim, yaş, göz rengi vs.)
    #Her objenin behaviour'ları vardır.(Metotlar)(yürümek, koşmak vs.)
#Functional Programming
#Procedure ORiented Programming


#Class - Design (blueprint)(taslak)
#Object - Instance(Örnek)


#Inheritence (Kalıtım)
#Encapsulation (Kapsülleme)
#Abstraction (Soyutlama)
#Polymorphism (Çok çeşitlilik)

#ÖRnek
#Televizyon
    #Üretim Yeri
    #Marka
    #Model
    #Ekran Boyutu
    #Şekil
    #Görüntü KAlitesi
    #Diğer Özellikler
    
    #Aç/Kapa
    #Kanal görüntüleme

#%%
# HAZIR GELEN SINIFLAR
a=5
print(type(a))

b=5.5
print(type(b))

c= "naber Gelmedi Senden Bir HAber"
print(type(c))

print(c)
print(c.capitalize())
print(c)# kalıcı olmadığını görüyoruz
# kalıcı olması için
c = c.capitalize()
print(c) # dememiz gerekiyor


liste=[4,3,7]
print(liste)
liste.sort()
print(liste) # sort için ise yapılan yenilik kalıcı oldu .



#%% KENDİ CLASSIMIZI (SINIFIMIZI - VERİ TİPİMİZİ OLUŞTURMA

class insan:
    #Attributes (Özellikleri) (Variables - Değişkenleri)
    #Behaviours (Davranışlar) (MEthods -Metotlar) (Fonksiyonlar)
    
    
    #isim,soyad,yas,meslek
    
    #constructor - yapıcı metot
    def __init__(self):
        pass

#i1 objesi insan sınıfının bir objesi
i1=insan()  #instantiate - oluşturmak

i1.ad="Mümine Aişe"
i1.soyad="demiral"
i1.yas=21
i1.meslek="bilgisayar mühendisi"

i2=insan()

i2.ad="Hafsa"
i2.soyad="demiral"
i2.yas=24
i2.meslek="Ergoterapist"

print(i1.ad,i1.soyad,i1.yas,i1.meslek)
print(i2.ad,i2.soyad,i2.yas,i2.meslek)


#%%DEVAMI

class insan:
    
    
    def __init__(self,ad,soyad,yas,meslek):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.meslek=meslek
        
    def bilgiSoyle(self):
        print("insanın Bilgileri")
        print("Adı Soyadı : {} {}".format(self.ad, self.soyad))
        print("Yaşı : {}".format(self.yas))
        print("Mesleği : {}".format(self.meslek))
        
i1=insan("Halime", "Demiral", 26 , "öğretmen")

i2=insan("şems","demiral",19, "yazılımcı")

#print(i1.ad,i1.soyad,i1.yas,i1.meslek)
#print(i2.ad,i2.soyad,i2.yas,i2.meslek)
insan.bilgiSoyle(i1)
insan.bilgiSoyle(i2)



#%% araba sınıfı modelleme

class Araba:
    def __init__(self,marka,model,yil,bakim):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.bakim=bakim
        
    def ozellikleriGoster(self):
        print(self.marka,self.model,self.yil,end=" ")
        self.bakimDurumunuGoster()
        
    def bakimDurumunuGoster(self):
        if self.bakim:
            print("Bakimi YApılmış")
        else:
            print("Bakımı yapilmamış")
        
        
a1=Araba("BMW","5,20",2022,True)
a2=Araba("Ferrari","P80/C",2015,False)

a1.ozellikleriGoster()
a2.ozellikleriGoster()

a1.bakimDurumunuGoster()
a2.bakimDurumunuGoster

a3=Araba(yil="2015",bakim=False,marka="Toyota",model="aa")
a3.ozellikleriGoster()


#%% 
#Variable Çeşitleri
# 1-) Instance Variable
# 2-) Class/Static Variable

class User:
    #Class namespace
    sayac=0
    def __init__(self,isim="isim yok",kayitTarihi = "20.12.2012"):
        #Object/Instance namespace
        User.sayac+=1
        self.isim=isim
        self.kayitTarihi=kayitTarihi
        
print(User.sayac)     
user1 = User("mümine aişe demiral","25.04.2005")
print(User.sayac)
print(user1.sayac)

user2 = User("HAlime Demiral","30.09.2001")
print(User.sayac)
print(user2.sayac)

del user2
USer.sayac_=1
print("Kullanıcı silindi")
print(user2.sayac)


#%% 
# Metot Çeşitleri
# 1-)Instance (Obje) Methods
# 2-)Class Methods
# 3-)Static Methods

class Calisan:
    sirket = "Turcell"
    
    def __init__(self,isim,soyad,sabitMaas,prim):
        self.isim=isim
        self.soyad=soyad
        self.sabitMaas=sabitMaas
        self.prim=prim
        
    #Obje Metodu
    def toplamMaas(self):
        return self.sabitMaas + self.prim
    
    #Sınıf Metodu
    @classmethod
    def sirketIsminiSoyle(cls):
        return cls.sirket
    
    @staticmethod
    def bilgi(info =None):
        if info != NOne:
            print(info)
        else:
            print("Çalışan sınıfına ait static metottur!!")
    
    
    
    
c1=Calisan("Aysel", "demiral", 55000, 1750)
c2=Calisan("Mehmet", "Demiral", 75000, 2000)

print(c1.toplamMaas())
print(c2.toplamMaas())

print(Calisan.toplamMaas(c1))
print(Calisan.toplamMaas(c2))

print(Calisan.sirketIsminiSoyle())
print(c1.sirketIsminiSoyle())
print(c2.sirketIsminiSoyle())


#%% 
# Inner Sınıflar
# sınıf içerisinde sınıf oluşturma

#Outer Class
class Musteri:
    def __init__(self,musteriNo,isim,soyisim,bakiye,hesapTuru):
        self.musteriNo = musteriNo
        self.isim = isim
        self.soyisim = soyisim
        #self.bakiye = bakiye
        #self.hesapTuru = hesapTuru
        self.hesap=self.Hesap(bakiye, hesapTuru)
        
    def bilgileriGoster(self):
        print(self.musteriNo,self.isim,self.soyisim)
        self.hesap.bilgileriGoster()
        
    #Inner Class
    class Hesap:
        def __init__(self,bakiye,hesapTuru):
            self.bakiye = bakiye
            self.hesapTuru = hesapTuru
            
        def bilgileriGoster(self):
            print(self.bakiye,self.hesapTuru)
            
m1 = Musteri(1, "Selim", "KApı", 5000, "TL")
m2 = Musteri(2, "Emel", "Toprak", 4500,"Dolar" )


m1.bilgileriGoster()
m2.bilgileriGoster()

hesap=Musteri .Hesap(6000, "Euro")
hesap.bilgileriGoster()

m1.hesap=hesap
m1.bilgileriGoster()





























