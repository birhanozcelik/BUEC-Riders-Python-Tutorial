"""
dict1 = {} -> bos dictionary
dict1 = {'name':'Birhan', 'age':24, 'address':'izmir'}
dict1.get('name') -> 'Birhan'
dict1['name'] -> Birhan
dict1.get('age') -> 24
dict1.get('address') -> address anahtari olmadigi icin hata vermez bos veri dondurur.
dict1['address'] -> hata verir
dict1['address'] = "izmir" -> address anahtarini sozluge(dictionary) ekler
dict1.pop(x) -> x anahtarını ve degerini sozlukten siler ve silinen degeri dondurur
dict1.popitem() -> rastegele bir anahtari siler ve degerini dondurur
dict1.clear() -> sozlugun icerigini siler
del dict1 -> sozlugu komple siler

dict1 = {'name':'birhan','age':24,'work':True}
for elm in dict1.items():
    print(elm)
"""

my_dict = {'name':'Birhan', 'addr':'izmir'}
print(my_dict.values())



