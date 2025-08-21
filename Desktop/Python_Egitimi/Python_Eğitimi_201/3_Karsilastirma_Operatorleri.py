#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 14:46:45 2025

@author: mumineaisedemiral
"""

a=10
b=15
c=20
d=20

# "==" Eşit mi?
print(a == b)# a b'ye eşit mi? FALSE
print(c == d)# c d'ye eşit mi? TRUE

# "!=" Eşit değil mi?
print(a!=b)#True
print(c!=d)#False

# ">" Büyük mü?
print(a>b)#False
print(b>a)#True
print(c>d)#False

print("{} > {} sorusunun cevabı : {}".format(a,b,a>b))

# "<" Küçük mü?
print(a<b) #True
print(b<a) #False
print(c<d) #False

# "<=" Küçük mü ya da eşit mi?
print(a <= b) #True
print(b <= a) #False
print(c <= d) #True

# ">=" Büyük mü ya da eşit mi?
print(a >= b) #False
print(b >= a) #True
print(c >= d) #True

#%%
#   Stringlerle Karşılaştırma İşlemleri
isim="Ali"
print(isim == "Ali")  #True
print(isim != "Ali")  #False
print(isim == "Kaan") #False
print(isim != "Kaan") #True

# ">" sözzlükte stringin sonra gelmesi
# "<" sözlükte stringin önce gelmsei
print("A"> "B") #False
print("A"<"B")  #True
#Küçük a nın büyük b ye olan durumunu ASCII alfabesine göre yorumlar.
print("a">"B") #False 

print("Ahmet">"Aise") #False

# PROBLEM ÇÖZÜMÜ
kelime1="ahmet"
kelime2="Mehmet"
#Bu iki kelimeyi karşılaştırmak için aşağıdakileri yaparız
kelime1 = kelime1.lower()
kelime2 = kelime2.lower()
print(kelime1 , kelime2)
print(kelime1 < kelime2)
