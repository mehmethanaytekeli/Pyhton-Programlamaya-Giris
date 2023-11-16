sayi=int(input("Faktöriyelini Hesaplayacağınız Sayıyı Giriniz"))
def faktör(sayi):
    return sayi*faktör(sayi-1)

print(faktör(sayi))

