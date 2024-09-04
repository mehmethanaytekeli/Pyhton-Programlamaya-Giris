def tambolme(sayi):
    tambolenler=[]
    for i in range(2,sayi):
        if (sayi % i ==0):
            tambolenler.append(i)
    return tambolenler

while (1):
    sayi = input("sayıyı girin:")

    print(tambolme(int(sayi)))
