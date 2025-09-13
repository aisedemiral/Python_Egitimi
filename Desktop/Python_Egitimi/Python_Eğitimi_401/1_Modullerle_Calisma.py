#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 14:38:27 2025

@author: mumineaisedemiral
"""

#Builtin Moduls
#import sys
#print(sys.builtin_module_names)

# EĞER BİR MODULDE OLAN FONKSİYONLAR BİRDEN FAZLA İSE VE BİZ YANLIZCA BİR TANESİNİ 
#KULLANACAK İSEK from benimModulum import topla vb kullanarak işlemimizi yapmalıyız.


from benimModulum import pi,daireCevreHesapla,daireAlanHesapla

#print(topla(20, 32))
print(pi)

#ovverride - geçersiz kılma (üzerine yazma)

from math import pi

print(pi)

#--------------
 
r=5
print(daireAlanHesapla(r))
print(daireCevreHesapla(r))



#%%  __name__ özel değişkeni

print(__name__)

import benimModulum as bm # as bm ile benimModulume bm takma adını vermiş olduk.

bm.daireAlanHesapla()



































