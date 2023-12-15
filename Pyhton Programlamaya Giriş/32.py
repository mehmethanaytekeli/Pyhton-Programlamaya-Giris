sayılar=[]
while 1:
    sayı=int(input("sayı eklemek için devam ediniz çıkmak için negatif değer giriniz"))
    if (sayı>0):
        sayılar.append(sayı)
    else:
        print(sayılar)
        break
