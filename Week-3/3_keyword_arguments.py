"""
def fonksiyon(param1,param2):
    print(param1,param2)

fonksiyon(param2="BUEC",param1="Riders")
keyword'lu argumandan sonra non-keyword arguman gelemez
fonksiyon(param2="BUEC","Riders") hata verir.
"""

def fonksiyon(param1,param2,param3):
    print(param1,param2,param3)
fonksiyon("Riders","Python",param3="Riders")