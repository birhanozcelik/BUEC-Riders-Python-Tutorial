"""
Bir string'i karakter dizesi olarak dusunebiliriz.

var = "Riders"

var[0] -> ilk karakter olan R karakterini dondurur.
var[0] = "E" -> Hata verir. String veri tipleri degistirilemezler.
var[7] -> Hata verir. Son indeks 5

List ve Tuple veri tiplerinde gordugumuz slicing islemini uygulayabiliriz.
var[1:4] -> 'ide' ciktisini verir. 

txt = "Python ile Programlamaya Giris"
x = txt.split()
x -> ["Python", "ile", "Programlamaya", "Giris"]

for dongusu ile iterasyon
for char in var:
    print(char)

del keyword u ile String tipindeki bir degiskenin karakterlerini silemeyiz.
del var[1] -> Hata verir.

Fakat, String tipindeki degiskeni tamamen silebiliriz.
del var 

"""

deger = "Python#ile#programlama#cok#guzel"

del deger

print(deger)
