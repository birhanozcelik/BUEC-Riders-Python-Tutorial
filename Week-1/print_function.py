#print(value, ..., sep='', end='\n', file=sys.stdout, flush=False)
"""
Yukarida print fonksiyonun alabilecegi parametleri görebilirsiniz.
value parametresi, terminale yazdirmak istedigimiz degerleri belirtmektedir.
Bu degerler, String, Integer, Float veya Boolean olabilir.

sep parametresi ise yazdirmak istedigimiz her degerin arasina default olarak bosluk koymaktadir.
Eger bosluk karatkeri yerine baska bir karakter koymak isterseniz bu paramtereyi degistirebilirsiniz.

end parametresi ekrana bastirilan degerin sonuna hangi karakterin yazilacagi anlamina gelmektedir.
Default olarak '\n' karakterini almaktadir. Bu karater terminalde gorunmemektedir. Görevi ise, islem 
bittikten sonra bir alt satira inmektir.

file ve flush parametrelerini su an icin gecebiliriz. İlerleyen derslerde deginebiliriz.
Merak eden arkadaslar arastirabilirler fakat yeni baslayanlar icin kafa karistirici olabilir.
"""

#Ornekler

print("Riders","BUEC","Python")
print("Riders", "BUEC", "Python", 2021, 17.18, True)
print("Riders","BUEC","Python", sep="-")
print("Riders","BUEC","Python", sep="-", end=".") # end parametresine \n yerine .(nokta) degerini verdigimiz
                                                  # icin curser bir alt satire inmedi bu nedenle, bir sonraki
                                                  # print fonksiyonu bir alt satirdan baslamayacak.
print("Riders","BUEC","Python", end=".\n")

