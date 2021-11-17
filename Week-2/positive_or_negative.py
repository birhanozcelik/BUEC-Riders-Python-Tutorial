for elm in range(3):
    user_input = int(input("Bir sayi giriniz: "))
    if user_input > 0:
        print("Sayi pozitif.")
    elif user_input < 0:
        print("Sayi negatif")
    else:
        print("Sayi sifir.")