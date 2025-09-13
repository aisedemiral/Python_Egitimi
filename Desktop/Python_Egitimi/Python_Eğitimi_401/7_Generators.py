#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:52:34 2025

@author: mumineaisedemiral
"""

# GENERATORS(ÜRETEÇLER)
# Her generator bir iteratördür.
# yield => verim, ürün

def sayiUret():
    yield 1            # yield ortaya ürün oluşturmal için kulllanılan anahtar kelimedir.
    yield True
    yield "Mümine Aişe Demiral"
    
uretilmisDegerler = list(sayiUret())

for sayi in uretilmisDegerler:
    print(sayi)

aralik = range(10)
print(list(aralik))

print(type(sayiUret))
print(sayiUret())
print(tuple(sayiUret()))


def ilkBinSayi():
    # yield 0 
    #yield 1
    #.
    #.
    #.
    #yield 1000
    
    i=0
    while i<=1000:
        yield i
        i+=1
        
print(list(ilkBinSayi()))
    
#%%

def katiniUret(sayilar,kati):
    for sayi in sayilar:
        yield sayi * kati
        
sayilar = [7,15,21,14]

sayilarin3Kati1 = katiniUret(sayilar, 3)

print(list(sayilarin3Kati1))

sayilarin3Kati2=[sayi * 3 for sayi in sayilar]

print(sayilarin3Kati2)


sayilarinKaresi=[sayi * sayi for sayi in sayilar]
print(sayilarinKaresi)



















