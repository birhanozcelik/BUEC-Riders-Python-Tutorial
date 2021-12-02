"""
Bir tuple icerisinde farkli elemanlar bulundurabilir.
my_tuple = (4,9,6,1)
my_tuple = ("Riders",2021,"BUEC")

Parantezleri kullanmadan da tuple veri tipi tanimlayabiliriz.
my_tuple = 1,"Riders",0,"BUEC"

Tek elemanli bir tuple olusturmak icin
my_tuple = (2) -> bu sekilde bir tanimlama tuple olusturmaz. Bu integer dır.
tuple olmasini istersek
my_tuple = (2,) -> bu tuple dır. Elemanin sonuna virgul(,) koymamiz yeterli.

tuple icerisnde bulunan elemanlar uzerinde for ile iterasyon
for elm in my_tuple:
    print(elm)

List konusunda gordugumuz indeks yapisinin aynisi tuple veri tipi de gecerlidir.
List konusunda gordugumuz slicing islemi tuple veri tipi icin de gecerlidir.

Tuple veri tipleri ile calisirken tuple icinde bulunan bir elamani degistiremezsiniz ve silemezsiniz!
Fakat del keyword u ile var olan bir tuple veri tipini silebilirsiniz.
del my_tuple

Tuple veri tipi ile calisirken kullanabileceginiz metodlar
my_tuple = (2,2,0,4)
my_tuple.count(x) -> tuple icerisinde kac tane x oldugunu verir
my_tuple.count(2) -> 2 degerini dondurur.

my_tuple.index(x) -> x degerinin indeksini verir
my_tuple.index(4) -> 3 degerini dondurur.

Daha detayli bilgi icin
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
"""

my_tuple = (1,2,3,"riders")
my_tuple[0] = 3
print(my_tuple)