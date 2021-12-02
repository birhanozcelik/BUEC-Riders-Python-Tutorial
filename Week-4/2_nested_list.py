"""
list icinde list tanimlayabiliriz.

my_list = ["a",["b", "c",  "d",  "e"]]
            0  [1,0] [1,1] [1,2] [1,3]

nested list uzerinde islem yapmak icin birden fazla dongu kullanmamiz gerekecektir.
"""

my_list = [[1,2,3,4,5],"a"]

for elm in my_list:
    for val in elm:
        print(val)

