#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:40:23 2025

@author: mumineaisedemiral
"""

class Arac:
    def __init__(self,tur):
        self.tur=tur
        
class Araba(Arac):
    def __init__(self):
        super().__init__("Araba")
    def calis(self):
        print("Motor çalıştı.")
        print("Hareket etmeye başlayabilirsin!")

class Motosiklet(Arac):
    def __init__(self):
        super().__init__("Motosiklet")

    def calis(self):
        print("Motor çalıştı")
        print("Motor ısınmaya başladı")
        print("Motorun ısınma süreci bitti")
        print("Hareket etmeye başlıyabilirsin.")




a1=Araba()
m1=Motosiklet()
a1.calis()
m1.calis()



class Insan:
    def git(self,arac:Arac):
        arac.calis()
        print("Hareket etmeye başladığım aracın türü:"arac.tur)
i1=Insan()
print(20*"*")
i1.git(a1)
print(20*"*")
i1.git(m1)
#%%
#OPERATOR OVERLOADING

toplam = 6 + 9
fullName = "Mümine"+"Aişe"

sonuc =c int.__add__(30,50)
sonuc = 30 + 50

takimIsmi = str.__add__("Galata", "Saray")
takimIsmi = "Galata" + "Saray"

#%% MAGIC METHODS (BÜYÜLÜ METOTLAR)

# addition(toplama işlemi) + operatörü
print(int.__add__(7, 8))
print(float.__add__(10.0, 5.0))

# substraction(çıkarma işlemi) - operatörü
print(int.__sub__(10, 2))

# multiplication (çarpma işlemi) * operatörü
print(int.__mul__(8, 9))
print(float.__mul__(13.2, 11.4))
print(str.__mul__('-', 30))

#division (bölme işlemi) / operatörü
print(int.__truediv__(16, 9))
print(int.__floordiv__(16, 9))
print(int.__divmod__(10, 3))
print(int.__divmod__(17, 4))


print([2,3,4,5,6].__len__()) #lenght
print(len([2,3,4,5,6,7]))

# greater than > operatörü
print(int.__gt__(5, 4))
print(5>4)

print(int.__gt__(4, 5))
print(4>5)

# greater or equal >= operatörü
print(int.__ge__(5, 5))
print(int.__ge__(5, 4))
print(int.__ge__(4, 5))

# lower than < operatörü
print(int.__lt__(5, 6))
print(int.__lt__(5, 4))

# lower or equal <= operatörü
print(float.__le__(10.2, 10.2))
print(float.__le__(10.2, 10.3))
print(float.__le__(10.2, 10.1))


#%%
from math import sqrt
class Nokta:
    sayac = 0
    def __init__(self,x,y):
        Nokta.sayac +=1
        self.x=x
        self.y=y
       
    # + operatörü
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y 
        return Nokta(x, y)

    def __str__(self):
        return f'({self.x},{self.y})'

    #>
    # noktaların orjine olan uzakllıkları
    def __gt__(self,other):
        u1 = sqrt(self.x*self.x+self.y*self.y)
        u2 = sqrt(other.x*other.x + other.y*other.y)
        return u1> u2
    
    def __len__(self):
        """
        
        1.bölgedeyse 1
        2.bölgedeyse 2
        3.bölgedeyse 3
        4.bölgedeyse 4
        Nokta orjindeyse 5
        y ekseni üzerindeyse 6
        x ekseni üzerindeyse 7

        """
        if self.x > 0 and self.y>0:
            return 1
        elif self.x<0 and self.y >0:
            return 2
        elif self.x <0 and self.y<0:
            return 3
        elif self.x >0 and self.y <0:
            return 4
        elif self.x ==0 and self.y ==0:
            return 5 
        elif self.x ==0:
            return 6
        elif self.y ==0:
            return 7
    
    
    def __del__(self):
        Nokta.sayac -=1
        print(f'{self} noktası kaldırıldı !!')

n1 = Nokta(5, 7)
n2 = Nokta(7,9)

n3 = n1 + n2

print(n3)

print(n1>n2)
print(n2>n1)

print(Nokta.sayac)

del n1
print(Nokta.sayac)

print("Noktamız {}.bölgededir.".format(len(n2)))


#%% 
#Metot overloading ve metot overriding

def topla (s1,s2):
    return s1+s2
def topla(s1,s2,s3=0):
    return s1 + s2+ s3

print(topla(2,5))
print(topla(2,5,9))




class Bina:
    def __init__(self,no):
        self.binaNo=no
    def adresSoyle(self):
        print("No:",self.binaNo)
        

class Daire(Bina):
    def __init__(self, no,binaNo):
        self.daireNo = no
        super().__init__(binaNo)
    # metot overriding
    def adresSoyle(self):
        print(f'Bina no: {self.binaNo} Daire no:{self.daireNo}')

b1 = Bina(68)
b1.adresSoyle()

d1=Daire(7,b1.binaNo)
d1.adresSoyle()























