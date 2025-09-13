#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 21:01:29 2025

@author: mumineaisedemiral
"""

sayi1 = 5
sayi2 = 5.5
print(isinstance(sayi1, int))
print(isinstance(sayi2,float))


class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(issubclass(A, B))
print(issubclass(B, C))
print(issubclass(C, A))
print(issubclass(B, A))


#%% Metotların Çözümlenme Sıralaması

class A:
    def metot1(self):
        print("A Metot 1")
    def metot2(self):
        print("A Metot 2")  

class B(A):
    def metot3(self):
        print("B metot 3")
    def metot4(self):
        print("B metot 4")
        
class C(B):
    def metot5(self):
        print("c metot 5")
    def metot1(self):
        print("C metot 1")

aObjesi = A()
bObjesi = B()
cObjesi = C()

aObjesi.metot1()
aObjesi.metot2()

bObjesi.metot3()

cObjesi.metot1() # kendine ait metot biri olduğu için önce kendi sınıfındaki metot biri çalıştırır.


#method resolution order
#metotun çözümleme sıralaması
C.mro()

# A super class(parent class)
# B sub class(child class)

# B->A single level inheritance
# C->B->A multi level inheritance 
# C->(A,B) multiple level inheritance

#%% mro örnek

class x:
    def metot1(self):
        print("x metot 1")
class Z:
    def metot1(self):
        print("z metot 1")
class Y:
    def metot1(self):
        print("y metot 1")
class A(X,Y):
   pass
class B(Y,Z):
    pass
class C(B,A,Z):
   pass
c1=C()
c1.metot1()



#%%
class D:
    def _init__(self):
        print("D contructor")
    def metot1(self):
        print("D metot 1")
class E:
    def _init__(self):
        print("E contructor")
    def metot1(self):
        print("E metot 1")
class F(D,E):
    def _init__(self):
        print("F contructor")
        super().__init__()
        D.__init__(self)
        E.__init__(self)
    def metot1(self):
        print("F metot 1")
        super().metot1()

fObj = F()
#fObj.metot1()
print(F.mro())

#%%

#Bir haber sitesinde haberler spor ve finans haberleri olmak üzere ikiye
#ayrılmaktadır. Her haberin başlığı, içeriği ve bir adet görseli bulunmaktadır.
#Spor haberleriinde video içerikleri de bulunmaktadır. finans haberlerinde
#döviz kurallarının bilgileri de yer almaktadır.Modelleyiniz


class GenelHaber:
    def __init__(self,baslik,icerik,gorsel):
        self.baslik=baslik
        self.icerik=icerik
        self.gorsel=gorsel
    def bilgileriGoster(self):
        print(self.baslik,self.icerik,self.gorsel)
        

class SporHaberleri(GenelHaber):
    def __init__(self, baslik, icerik, gorsel,video):
        super().__init__(baslik, icerik, gorsel)
        self.video=video
    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(self.video)  
        
    def videoOynat(self):
        print(self.video," isimli video oynatılıyor...")
        
class FinansHaberleri(GenelHaber):
    def __init__(self, baslik, icerik, gorsel,dovizKurlari):
        super().__init__(baslik, icerik, gorsel)
        self.dovizKurlari=dovizKurlari
    def dovizKurlariBilgisiniGoster(self):
        for dovizAdi,dovizDegeri in self.dovizKurlari.items():
            print(dovizAdi,":",dovizDegeri)
    def dovizKurlariniGuncelle(self,dovizKurlari):
         self.dovizKurlari=dovizKurlari

s1 =SporHaberleri(video="video1.mp4",baslik="maçta kazanan olmadı",icerik ="0-0 bitti!",gorsel="foto1.png")
f1=FinansHaberleri(baslik="Ekonomi tüm dünyada durgun", icerik="küresel salgın tüm dünyayı etkiledi", gorsel="foto2.png", dovizKurlari = {'Dolar':17,'Euro':17.5,'Sterlin':20})

f1.dovizKurlariBilgisiniGoster()
s1.bilgileriGoster()

guncelKurBilgisi =  {'Dolar':17.1,'Euro':17.6,'Sterlin':20.1}
f1.dovizKurlariniGuncelle(guncelKurBilgisi)
f1.dovizKurlariBilgisiniGoster()



































