kullanıcı_sayısı=0
kullanıcı_sayısı=int(input("faktoriyeli değer giriniz:"))
faktoriyel=1
if (kullanıcı_sayısı==0):
    print("1")

elif(kullanıcı_sayısı<0):
    print("yanlış değer girildi")
else:
    while kullanıcı_sayısı>0:
        faktoriyel=kullanıcı_sayısı*faktoriyel
        kullanıcı_sayısı=kullanıcı_sayısı-1

    print(faktoriyel)

