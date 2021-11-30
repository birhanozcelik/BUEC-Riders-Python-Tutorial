"""
ic ice fonksiyonlar kullanirken nonlocal keyword'une ihtiyacimiz olabilir.
eger, ic fonksiyon dis fonksiyonun degiskenini degistirmek isterse
ic fonksiyonda o degiskenin basina nonlocal keyword'unu yazmamiz gerekir.
"""

def fonksiyon1():
  deger1 = 10
  def fonksiyon2():
    nonlocal deger1
    deger1 = 15
    print(deger1)
  fonksiyon2()
  print(deger1)

fonksiyon1()