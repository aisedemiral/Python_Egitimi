#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 22:09:07 2025

@author: mumineaisedemiral
"""

#PRINT FONKSİYONLARI
"""
end parametresi python fonksiyonunda default olarak \n ile tanımlanır 
eğer biz end parametresine end=" " dersek artık aralarında sadece boşluk olmuş olur.
"""
print("Python")
print("Eğitimi")
print("Python",end=" ")
print("Eğitimi")

#sep=" "
"""
normade seperatet fonksiyonuna default olarak boşluk tanımlanırken alt tarafta sep fonksiyonuna
 - ile ayrılması gerektiğini atamış olduk
"""
print("Fatih","Kaan","Açıkgöz")
print("Fatih","Kaan","Açıkgöz",sep="-")


print(7,5,2004,sep="/")
print("01","01",2025,sep="/")

print("TC")
#TC in başına koyduğumuz * ile tırnak işareti içerisindeki elemanları boşlukla ayırması gerektiğini söyleriz.
print(*"TC")
print(*"TC",sep=".")