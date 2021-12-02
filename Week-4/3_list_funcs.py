"""
iki ayri list'i + operatoru ile birlesitirebiliriz.
a = [0,2,6]
a += [4,7,9]
a -> [0,2,6,4,7,9]

List'ler ile calisirken kullanabilecegimiz fonksiyonlar
my_list = [0,2,4]

append(x) -> listenin sonuna x degerini ekler(bir tane)
my_list.append(5) -> [0,2,4,5]

insert(i,x) -> listenin i. indeksine x degerini ekler
my_list.insert(1,1) -> [0,1,2,4,5]

pop([i]) -> i. indekste bulunan elemani dondurur(eger belirtilmemis ise son elemani dondurur) ve o indeksteki elemani listeden siler
my_list.pop() -> [0,1,2,4] -> indeks belirtilmedigi icin 5 degerini dondurur.

clear()  -> listeden tum elemanları siler.
my_list.clear() -> [] my_list hala mevcut ama ici bos

extend(iter) -> listeye birden fazla eleman ekler
my_list.extend([0,1,2,3,4]) -> [0,1,2,3,4]

remove(x) -> x degerini listeden siler eger o deger yoksa hata dondurur
my_list.remove(5) -> hata dondurur cunku listede 5 diye bir eleman yok
my_list.remove(1) -> 1 degerini listeden siler -- 1. indekste bulunan elemani degil!

del a_list[i] -> i. indekste bulunan elamani siler ayrica tum listeyi silmek icin de kullanilir.
del my_list[0] -> [1,2,3,4]]
del my_list -> my_list artik mevcut degil

Ayrica, bir listenin eleman gruplarina bos liste atayarak da o elemanlari silebiliriz.
my_list = ['B','0','1','2','U','E','C']
my_list[1:4] = []

Daha detayli bilgi icin,
https://docs.python.org/3/tutorial/datastructures.html
"""

my_list = ["a","b","c","d","e","f"]
print(len(my_list))
my_list[2:5] = []
print(len(my_list))
