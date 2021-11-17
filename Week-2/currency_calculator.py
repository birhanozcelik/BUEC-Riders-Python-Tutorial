# $, €, £

while True:

    birim = input("Para birimini giriniz (€,$,£): ")
    miktar = float(input("Miktari giriniz: "))

    if birim == "$":
        print("{} {} = {:.2f} TL".format(miktar,birim,miktar*10.5))
    elif birim == "€":
        print("{} {} = {:.2f} TL".format(miktar,birim,miktar*11.4))
    elif birim == "£":
        print("{} {} = {:.2f} TL".format(miktar,birim,miktar*13.4))
    else:
        print("Lutfen gecerli bir para birimi giriniz!")
    
    devam_mi = input("Devam etmek ister misiniz? (E/H): ")
    if devam_mi == "H":
        print("islem sonlandirildi.")
        break 
        