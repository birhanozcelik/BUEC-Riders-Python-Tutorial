"""
if kosul1 and kosul2 and .. and kosuln:
    kosul veya kosullar True ise bu blok calisacak.
elif kosula and kosulb and .. and kosulz:
    if kosulu False ise program ilk bu blok calisacak.
else:
    kosulların tamami False ise bu blok calisacak.
"""

number1 = 13
number2 = 13
if number1 > number2:
    print("{} degeri, {} degerinden buyuktur.".format(number1,number2))
elif number2 > number1:
    print("{1} degeri, {0} degerinden buyuktur.".format(number1,number2))
else:
    print("iki deger birbirine esit.")
