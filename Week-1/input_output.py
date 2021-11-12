"""
input fonksiyonu, komut satirindan deger girilebilmesi icin kullanilir.
Girilen deger veya degerler default String olarak alinmaktadir. Bu nedenle, aritmetik islem yapacaksaniz
tur donusumu yapmayi unutmayin.
"""

name = input("Isminizi giriniz: ")
print("Merhaba, ",name)
print(type(name)) #tur donusumu yapmadigimiz icin name degiskeni String tipinde

# Aritmetik islemler

number = int(input("Bir sayi giriniz: ")) #String turuden integer'a tur donusumu yaptik
                                          #Cunku String veri tipi ile aritmetik islemler yapamayiz.
sonuc = number * 2
print("Girdiginiz sayinin iki kati: ",sonuc)