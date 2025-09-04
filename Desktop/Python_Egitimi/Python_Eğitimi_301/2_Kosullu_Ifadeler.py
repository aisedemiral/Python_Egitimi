#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 16:14:58 2025

@author: mumineaisedemiral
"""

yas=int(input("lütfen yaşınızı giriniz"))



if yas<18:
    print(f"{yas} yaşındasınız.Reşit Değilsiniz!!!")
else:
    print(f"{yas} yaşındasınız.Reşitsinizzz.")
       
    
if yas>=18:
    print(f"{yas} yaşındasınız.Reşitsiniz.")
else:
    print(f"{yas} yaşındasınız.Reşit Değisiniz!!!")
    
    
#******************************************

sayi=int(input("Lütfen bir sayı giriniz."))

if sayi/2==0:
    print(f"{sayi} . Girdiğiniz sayı çiftir.")
else:
    print(f"{sayi} . Girdiğiniz sayı tektir.")
    
    #TYPE CASTİNG 0 DIŞINDAKİ HER SAYININ BOOLEAN DEĞERİ TRUE'DUR.
    
#%% İÇ İÇE İF ŞARTLI KONTROL YAPISI

# vizesi %60 etkili 
#ortalaması 50 ve üzeri olanlar dersi geçiyor.

vize=int(input("Lütfen vize notunuzu giriniz"))
final=int(input("Lütfen final notunuzu giriniz."))
if final >= 50:
    ort = (vize*60)/100+(final*40)/100
    if ort>=50:
        print(f"{ort} ortalama ile - Tebrikler dersi geçtiniz.")
    else:
        print(f"{ort} ortalama ile Üzgünüm dersten kaldınız. Seneye tekrar deneyiniz.")
else:
    print("Final notunuz yüzünden dersten kaldınız.")
    
#%% ay bilgisine göre mevsim bulma kodu

ay=input("Lütfen ay ismini giriniz")


if ay== "aralık" or ay=="ocak" or ay=="şubat":
    print("şu anda kış mevsimini yaşıyorsunuz.")
elif ay=="mart" or ay=="nisan"or ay=="mayıs":
    print("şu anda ilkbahar mevsimini yaşıyorsunuz.")
elif ay == "haziran" or ay=="temmuz" or ay=="ağustos":
    print("şu anda yaz mevsimini yaşıyorsunuz.")
elif ay=="eylül" or ay=="ekim" or ay=="kasım":
    print("şu anda kış mevsimini yaşıyorsunuz")
else:
    print("yanlış bir string girdiniz.")
    
    
#%% cinsiyet ve boy uzunluğuna göre mülakatı geçme durumu örneği
#kadınlarda 160 erkeklerde 170 sınır 
#sınırı geçen ön sağlık muaynesini geçebilir.

print("*******ÖN SAĞLIK MUAYNESİNE HOŞGELDİNİZ******")
cinsiyet=input("Lütfen cinsiyetinizi giriniz: |Kadın veya Erkek| ")
if cinsiyet == "Kadın":
    kadınBoy=float(input("Hanımefendi lütfen boyunuzu giriniz:(m)"))
    if kadınBoy>=1.60:
        print("Tebrikler ön sağlık muaynesini geçtiniz.")
    else:
        print("Üzgünüz ön sağlık muaynesnden kaldınız.")
        
elif cinsiyet == "Erkek":
    erkekBoy=float(input("Beyfendi lütfen boyunuzu giriniz (m): "))
    if erkekBoy>1.70:
        print("Tebrikler ön sağlık muaynesini geçtiniz.")
    else:
        print("Üzgünüz ön sağlık muaynesinden kaldınız.")
else:
    print("Lütfen geçerli bir cinsiyet giriniz: Kadın veya Erkek")
    
#VEYA İKİ KONTOLU TEK SATIRDA AND İBARESİ İLE YAPABİLİRSİNİZ.

#%%
cinsiyet="kadın"
boy=30
if (cinsiyet=="kadın" or cinsiyet=="erkek") and (boy<300 and boy>20):
    if cinsiyet=="kadın" and boy==160:
        print("Ön sağlık muaynesini geçtiniz tebrikler.")
    elif cinsiyet=="erkek" and boy==170:
        print("Ön sağlık muaynesini geçtiniz tebrikler.")
    else:
        print("Ön sağlık muaynesinden elendiniz.")
    
    
else:
    print("lütfen cinsiyet için yanlızca kadın veya erkek giriniz ve boyunuzu da [20,300] aralığında tutunuz.")
   
#%% KULLANICIDAN 3 TANE SAYI ALAN VE BU 3 SAYIDAN EN BÜYÜK VE EN KÜÇÜK DEĞERİ SÖYLEYEN PROGRAM

sayi1 = int(input("Lütfen 1.sayıyı giriniz: "))
sayi2 = int(input("Lütfen 2.sayıyı giriniz: "))
sayi3 = int(input("Lütfen 3.sayıyı giriniz: "))
print(sayi1,sayi2,sayi3)

buyuk=sayi1
kucuk=sayi1

if sayi1<sayi2 or sayi1<sayi3:
    buyuk=sayi2
    if sayi2<sayi3:
        buyuk=sayi3
if sayi1>sayi2 or sayi1> sayi3:
    kucuk=sayi2
    if sayi2>sayi3:
        kucuk=sayi3
        
print("{} {} {} sayıları arasında küçük olan: {}".format(sayi1,sayi2,sayi3,kucuk))
print("{} {} {} sayıları arasında büyük olan: {}".format(sayi1,sayi2,sayi3,buyuk))

    
#*************************************
#Bu işlemi python nimetleri ile yapalım (daha fazla sayılar verildiğinde bu methotları kullanmak bizim lehimize olacaktır.)
sayilar=[sayi1,sayi2,sayi3]
    
print("{} {} {} sayıları arasında küçük olan: {}".format(sayi1,sayi2,sayi3,min(sayilar)))
print("{} {} {} sayıları arasında büyük olan: {}".format(sayi1,sayi2,sayi3,max(sayilar)))

    
#%% KULLANICI ADI VE ŞİFRE KONTROLÜ YAPAN PROGRAM

adminAdi="admin123"
adminSifre="pass123"

kullaniciAdi=input("Lütfen kullanıcı adınızı giriniz:")
kullaniciSifre=input("Lütfen şifrenizi giriniz:")

if kullaniciAdi==adminAdi and kullaniciSifre==adminSifre:
    print("Sisteme başarılı bir şekilde giriş yaptınız.")
elif  kullaniciAdi==adminAdi:
    print("lütfen şifrenizi doğru giriniz")
else:
    print("bilgilerinizi kontrol ederiz.")
    
    
#%% KENARLARINA GÖRE ÜÜÇGEN BİLGİSİNİ SÖYLEYEN PROGRAM

knr1=int(input("Lütfen 1.kenarı giriniz:"))
knr2=int(input("Lütfen 2.kenarı giriniz:"))
knr3=int(input("Lütfen 3.kenarı giriniz:"))

#absolute value = mutlak değer
if abs(knr1-knr2) <knr3 and (knr1+knr2)>knr3:
    if knr1==knr2 and knr2==knr3:
        print("bu bir eşkenar üçgendir.")
    elif knr1 ==  knr2 or knr1==knr3 or knr2==knr3:
        print("bu bir ikizkenar üçgendir.")
    else:
        print("bu bir çeşitkenar üçgendir.")
    
#%% ASCI TABLOSU
# A-Z 65-90 #26 Harf
# a-z 97-122 #26 Harf

harf=input("Lütfen bir harf giriniz:")
#print(harf)

if len(harf)==1:
    if ord(harf)>=65 and ord(harf)<=90:
        print("{} büyük harftir.".format(harf))
    elif ord(harf)>=97 and ord(harf)<=122:
        print("{} küçük harftir.".format(harf)
    else:
        print("girdiğiniz karakter latin alfaabesinde bulunamamaktadır.")
else :
    print("Lütfen sadece 1 karakterli harfi giriniz.")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
