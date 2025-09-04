#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 22:41:04 2025

@author: mumineaisedemiral
"""
#integer
sayi1=155
sayi2=167
print(sayi1)
print(sayi2)

print("1deneme".isidentifier())#isidentifier kullanarak tırnak içindeki ifadeyi değişken adı olarak kullanıp kullanamıyacağımızı öğreniriz.
print("deneme1".isidentifier())


#%% float
sayi1=165
sayi2=57

print("Toplama:",sayi1+sayi2)
print("Çıkartma:",sayi1-sayi2)
print("Çarpma:",sayi1*sayi2)
print("Bölme:",sayi1/sayi2)

print(type(sayi1))
print(type(sayi2))

print(id(sayi1))
sayi3=165
print(id(sayi3))

#%%

sayi1=15.4
sayi2=16.3

print("Toplama:",sayi1+sayi2)
print("Çıkartma:",sayi1-sayi2)
print("Çarpma:",sayi1*sayi2)
print("Bölme:",sayi1/sayi2)

print(sayi1,type(sayi1))
print(sayi2,type(sayi2))

# eğer sayıda nokta varsa o makine için kesirli bir sayıdır mesela 15.0 insan gözünde bir integer olsa bile makine için kesirli sayıdır.

#%% str(string)
isim="Mümine Aişe"
soyad="Demiral"

print(isim,type(isim))
print(soyad,type(soyad))


print(len(isim))
print(len(soyad))

print(isim,soyad)

#concetenate
ismintamami=isim +" "+soyad
print(ismintamami)

print(ismintamami[0],ismintamami[4],ismintamami[8],sep=".")

#%%

kelime="Galata"
print(kelime)
kelime="salata"
print(kelime)

#Immutable(Değiştirilemez)
"""
str şeklindeki kelimelerin herhangi bir harfini değiştirmek istediğimizde doğrudan değiştiremeyiz
bunada Immutable denmektedir.
"""

kelime= "M"+kelime[1:]#m+ birinci karakterlerden itibarenki kelimelerdir.
print(kelime)

takim="Galatasaray"
kelime1=takim[0:6]
kelime2=takim[6:]

print(kelime1)
print(kelime2)

kelime3=takim[3:6]
print(kelime3)


yer="İstanbul"
print(yer[0::2]) # sıfırdan başla ikişer ikişer sonuna kadar gel. START ,STOP ,STEP

isim="kaan"
print(isim[::-1])

isim2="diyarbakır"
print(isim2[7:4:-1])

#%%                     Objelerin RAM'de toplanması

#RAM in heap bölgesinde tutulur

import sys
sayi=111111
str1="Python Eğitimiiiiii"
print(sys.getsizeof(sayi))
print(sys.getsizeof(str1))

#%%                     Type Conversion (Tip Dönüşümü)

x=6
y=5.8
z="185"

print(int(y))
print(float(x))


print(z*2)
print(int(z)*2)

z="a185"
#print(int(z))
#print(float(z))

z="8.7"
print(float(z))#str yi floata çevirme
print(int(float(z))) #str yi önce floata sonra inte çevirme

print(17/6)
print(int(17/6))

#int->float
print(float(7))
#str->float
print(float("16.8")*2)



#%%   Kullanıcıdan girdi alma (input alma)

girdi=input("lütfen bir girdi giriniz:")
print("Girdiğiniz kelime: ",girdi)

sayi1=input("Lütfen 1.sayıyı giriniz:")
print("sayının 5 katı =",5*sayi1)














