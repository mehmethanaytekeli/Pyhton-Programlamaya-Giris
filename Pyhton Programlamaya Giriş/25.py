def mukkemmel_sayi(muk):
    toplam=0
    mukemmeller = []
    for j in range(2,muk):
        for i in range(1,j):
            if (j % i ==0):
                toplam+=i

        if (j == toplam):
             print(toplam,"mükemmel sayıdır")
             toplam = 0
             mukemmeller.append(j)
        else:
             print(j,"mükemmel sayı değil")
             toplam = 0
    print("mükemmel sayilar:",mukemmeller)
muk=int(input("Kaça Kadar?"))
print(mukkemmel_sayi(muk))