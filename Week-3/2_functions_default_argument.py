"""
def fonksiyon_adi(param1,param2="BUEC"):
    print(param1,param2)

fonksiyon_adi("param1")

Fonksiyonu cagirirken tek parametre verebiliriz. 
Bu deger param1 parametresine karsilik gelir.
param2 ise opsiyoneldir. Eger, deger vermezsek default olarak BUEC degerini alir.

def fonksiyon2(param1="BUEC",param2)
Bu fonksiyon hata verecektir.
Default argumanlardan sonra non-default argumanlar gelemez.
"""

def kullanici_bilgileri(name,age=24,sehir="İstanbul"):
    print("Merhaba {}. Yasiniz: {}. Yasadiginiz sehir {}".format(name,age,sehir))

kullanici_bilgileri("Birhan","İstanbul")
