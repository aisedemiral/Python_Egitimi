#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 15:12:21 2025

@author: mumineaisedemiral
"""

onerme1= "Galatasaray bir futbol takımıdır."
onerme2= "Galatasaray dünyanın en iyi futbol takımıdır."
onerme3= "Fenerbahçe bir futbol takımıdır."
onerme4= "Fenerbahçe dünyanın en iyi futbol takımıdır."

o1 = " True" #1
o2 = "False" #0
o3 = "True"  #1
o4 = "False" #0

# or and not 

#  or TABLOSU
#or| o1 o2 | s
#***************
#  | 0  0  |0
#  | 0  1  |1
#  | 1  0  |1
#  | 1  1  |1


# and TABLOSU
#and| o1 o2 | s
#****************
#   | 0  0  | 0
#   | 0  1  | 0
#   | 1  0  | 0
#   | 1  1  | 1


# not TABLOSU
#not| o | s
#************
#   | 0 | 1
#   | 1 | 0

#%%
# MANTIKSAL OPERATÖRLERLE İLGİLİ ÖRNEKLER

a=10
b=15

a,b=10,15
c,d,e=20,25,30

print("OR")
print(a<15 or b<20)
print("{} or {} ={}".format(a<15, b<20,a<15 or b<20))
print("{} or {} ={}".format(a<10, b<20,a<10 or b<20))
print("{} or {} ={}".format(a<15, b<15,a<15 or b<15))
print("{} or {} ={}".format(a<10, b<15,a<10 or b<15))


print("NOT OPERATÖRÜ")
anahtar= True
print(anahtar)
anahtar = not anahtar
print(anahtar)

sonuc=not(a<15 and b<20 or c<25 and d<30)
print(sonuc)

#%%

k1 = 4<5
k2 = 5>6
k3 = 7<=7
print(k1,k2,k3)
sonuc1 = bool("Ahmet") # True
sonuc2 = bool(5)       # True
sonuc3 = bool(4.8)     # True


import sys
print(sys.getsizeof(5))
print(28*8)


sonuc4=bool("") #False
sonuc5=bool(0)  #False
sonuc6=bool(0.0) #False

sonuc7=bool(" ") #True

# ASCII tablosuna göre cevapları vermiştir.


#%%
#    Tek Terimli Operatörler
# + - ~
x=+-+--2
y=---x
z=++++++++15
print(z)
z=-z
print(z)

#bitwise bazında operatör(bit bazında)
t = 5 #0101 #işaret bitleri 0 pozitif 1 negatif
m = ~t #(0101)'=1010


#-A  = A' +1
#A'  = -A - 1
#    = 1010 - 0001
#    =1001
#A = (A')' = (1001)' = 0110 =Onluk tabanda +6


#%%
# is   is not

x = 5
y = 5

#type() value(değer)          
print(x is y)# False            # hem tip hem değer bakımından eşit olması gerekiyor.
print(x == y)# True
print(x is not y)# True
print(x != y) # False

k1= 2 < 3
print((2<3) is True)
print(type(2<3),2<3)



#%%
# Bitwise (Bitsel) Operatörler
# &  |  ~  ^  <<  >>

x = 3 #001
y = 2 #010
sonuc1 = x & y 



#%%
# in not in

kelime = "Türkiye"
print("ü" in kelime)
print("t" in kelime)
print("ye" in kelime)
print("ey" in kelime)

liste=[1,2,3]

print(1 in liste)
print(3 in liste)
print(2 in liste)
print(4 in liste)

print("g" not in kelime)
print(5 not in liste)
print("r" not in kelime)

































