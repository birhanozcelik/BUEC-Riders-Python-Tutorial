"""
my_list = [values]

Bir list, icinde farkli tipte elemanlar bulundurabilir

list icinde bulunan elemanlar uzerinde for ile iterasyon
for elm in my_list:
    print(elm)

my_list = ["a","b","c","d"]
            0   1   2   3
            -4  -3  -2  -1
list icerinde bulunan elemanlara erisebilmek icin [] kullanabiliriz.
my_list[0] -> "a"
my_list[3] -> "d"

len(my_list) -> 4

list slicing
                  0   1   2   3   4   5
my_list =       ['R','I','D','E','R','S']
my_list[1:4] ->     ['I','D','E']
my_list[2:]  ->         ['D','E','R','S']
my_list[:4]  -> ['R','I','D','E']

Daha etkili bir sekilde list olusturmak
a = [x for x in range(5) if x % 2 == 0]
a -> [0,2,4]
"""

my_list = ["Riders","BUEC","PYTHON",2021]
my_list[-1] = "Programlama"
print(my_list)




