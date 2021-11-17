input_value = int(input("Bir tane sayi giriniz: "))

if input_value > 0 and input_value%2 == 0:
    print("Girdiginiz sayi pozitif ve cifttir.")
elif input_value > 0 and input_value%2 != 0:
    print("Girdiginiz sayi pozitif ve tektir.")
elif input_value < 0 and input_value%2 == 0:
    print("Girdiginiz sayi negatif ve cifttir.")
elif input_value < 0 and input_value%2 != 0:
    print("Girdiginiz sayi negatif ve tektir.")
else:
    print("Girdiginiz sayi sifir.")
