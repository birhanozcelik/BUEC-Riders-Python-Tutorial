"""
Kendini yineleyen fonksiyonlara recursion function denir.
"""

def faktoriyel(deger):
    if deger == 1:
        return 1
    else:
        return(deger * faktoriyel(deger-1))

print(faktoriyel(5))
"""
faktoriyel(5) -> = 120
"""

    