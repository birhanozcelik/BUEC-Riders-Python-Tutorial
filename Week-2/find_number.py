random_value = 25
user_input = int(input("Bir sayi giriniz: "))
while True:
    if user_input > random_value:
        print("Asagi")
    elif user_input < random_value:
        print("Yukari")
    else:
        break
    user_input = int(input("Bir sayi giriniz: "))

print("Dogru tahmin ettiniz!")
        