#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:26:40 2025

@author: mumineaisedemiral
"""
from abc import ABC,abstractmethod
class Makine(ABC):
    @abstractmethod
    def calis(self):
        print("Makine Çalıştı !!")
    
class CamasırMakinesi(Makine):
    def calis(self):
        print("Çamaşır makinesi çalıştı.")
        
class BulasikMakinesi(Makine):
    def calis(self):
        print("Bulaşık makinesi çalıştı")

c1 = CamasırMakinesi()
b1 = BulasikMakinesi()

c1.calis()
b1.calis()



# ABSTRACK METOTLARIN KESİNLİKLE DOLDURMAK GEREKİYOR

class Insan:
    def camasirYika(self,makine:CamasırMakinesi):
        if type(makine) == CamasırMakinesi:
            print("insan çamaşırları makineye attı.")
            makine.calis()
        else:
            print("Bu makinede çaaşır yıkayamazsın!!!")
            
i1 = Insan()
i1.camasirYika(c1)

i2=Insan()
i2.camasirYika(b1)











