"""
Belirli bir siralari yoktur. Set'ler indeks kavramina sahip degildir.
Elemanlar degistirilemezler.
Elaman ekleme ve cikarma islemi yapabiliriz.
Tekrarli elamanlara izin verilmez.
Farkli tipte veriler tutabiliriz.

set1 = {7,5,9}
set2 = {} -> bu bir set degildir. Ici bos bir set olusturmak istersek eger,
set3 = set() -> set fonksiyonunu kullanabiliriz.

set veri tipi ile calisirken indeksleme ve slicing gibi yaklasimlar yapamayiz.

set1.add(x) -> x degerini ekler. Tek bir deger eklemek istersek add metodunu kullanabiliriz.
set1.add(3) -> {3,5,7,9}
set1.update([val1,val2,val3,..]) -> Birden fazla deger eklemek istersek update metodunu kullanabiliriz.
set1.update([4,6,7],{0,2,9}) -> {0,2,3,4,5,6,7,9}
set1.discard(x) -> x degerini cikarir. Eger, x set icerisinde yoksa bir degisiklik yapmaz ve hata vermez.
set1.discard(0) -> {2,3,4,5,6,7,9}
set1.discard(0) -> 0 degeri set icerisinde yok bu nedenle bir degisiklik yapmaz ama hata da vermez.
set1.remove(x) -> x degerini set icerisinden cikarir. Eger, x degeri yoksa hata verir.
set1.remove(0) -> Hata verir cunku 0 degeri set icerisinde yok
set1.remove(2) -> {3,4,5,6,7,9}
set1.pop() -> rastgele bir degeri set icerisinden cikarir ve geri dondurur. 
set2 = {2,3,4}
set1.union(set2) -> set1 ve set2 kumelerini birlestirir.
set1.intersection(set2) -> iki kumenin kesisimini verir.
Daha detayli bilgi icin
https://docs.python.org/3/tutorial/datastructures.html#sets
"""

set1 = {1,2,3,4,5,6}
set2 = {4,5,3}

print(set2.issubset(set1))

