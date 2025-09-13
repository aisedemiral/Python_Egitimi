#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 22:04:50 2025

@author: mumineaisedemiral
"""

""" Errors (Hatalar)"""
#Exception (Olağandışılık, istisna)
#Handling (İşleme, idare etme)

#1-) Compile time errors(Derleme zamanı hataları)
    #Syntactical Errors(Dil bilgisi hataları)
        # : işaretini for veya if'in sonuna koymamak gibi hatalar.
#2-) Logical errors(Mantıksal Hatalar)
    #Wrong output (yanlış çıktı)
        # Fonksiyonu 5 ve 6 sayılarını gönderiyorsun
        # ama sonuç olarak 10 çıkıyor
        # 11 çıkmıyor gibi hatalar. (Mantıksal hatalar)
#3-) Run time errors(Çalışma zamanında hatalar)
    #Divide by zero (Sıfıra bölme)
        #Bir sayıyı 0'a böldüğümüz zamanki gibi çıkan hatalar.
#Statement
    #Normal (Warning - Uyarı)
    #Critical (Error - Hata)

#%%

# ValueError (Değer Hatası)
# ZeroDivisionError (Sıfıra Bölme Hatası)

try:
    #raise ValueError
    sayi1 = int(input("Lütfen bir tam sayı giriniz: "))
    sayi2 = int(input("Lütfen bir tam sayı giriniz: "))
    print(f'{sayi1}/{sayi2}={round(sayi1/sayi2,3)}')

except ValueError:
    print("LÜTFEN TAM SAYI GİRİNİZ.")

except ZeroDivisionError:
    print("Hiçbir reel sayı sıfıra bölünemez !! Lütfen ikinci sayıyı sıfır dışında bir sayıya bölünüz.")


#%%
sayi1=9
sayi2=0

try:
    sayi2=int(input("Sayı giriniz: "))
    print(sayi1/sayi2)
except Exception as e:
    print("Karşılaşılan hata: ", e)

#%%

sayi1=10
sayi2=0
try:
    print("Dosya açıldı!!")
    print(sayi1/sayi2)
except Exception as e:
    print("Hata: ",e)
finally:
    print("dosya kapandı !!")


#%%

def fact(n):
    if n< 0 or type(n) != int:
        raise ValueError("Sayı doğal sayı olmalıdır!!")
    if n==0:
        return 1
    return n* fact(n-1)

try:
    print(fact(6))
    print(fact(-5))
except Exception as e:
    print("Hata : ",e)















