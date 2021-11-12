deger1 = 24
deger2 = 36
toplam = deger1 + deger2

#Koseli parantezlerin icine indeksleri vermezsek eger sirasiyla degerleri basacaktir
print("{} + {} isleminin sonucu = {}".format(deger1,deger2,toplam))
#Koseli parantezler icerisine indeksleri verirsek eger indekslere gore degerleri basacaktir.
#Asagidaki ornek yukaridakiyle ayni islemi yapmaktadir.
print("{0} + {1} isleminin sonucu = {2}".format(deger1,deger2,toplam))
#Asagidaki ornekte indekslerin yerlerini degistirdik. Farki inceleyiniz.
print("{1} + {0} isleminin sonucu = {2}".format(deger1,deger2,toplam))