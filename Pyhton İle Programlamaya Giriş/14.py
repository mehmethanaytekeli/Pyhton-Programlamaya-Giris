baz=5000
prim=8
maas=0
print("***************************************************\n*                      Maaş                       *\n*                  Hesaplayıcısı                  *\n***************************************************")
print("|1.Patron Arayüzüne Giriş                         |\n|2.Çalışan Arayüzü Giriş                          |")
a=int(input("|Girilecek Arayüzü Seçiniz                        |"))
if (a==1):
    print("***************************************************\n|1.Baz Maaşı Ayarlama({})                       |\n|2.Prim Yüzdesi Ayarlama({})                       |".format(baz,prim))
    a= int(input("|Girilecek Arayüzü Seçiniz                        |"))
    if(a==1):
        baz=int(input("|Baz Maaşı Kaç Olarak Değiştirmek İstersiniz      |"))
    elif(a==2):
        prim=int(input("|Baz Primi Kaç Olarak Değiştirmek İstersiniz      |"))
    else:
        print("|Yanlış Değer Girildi Kod Sonlandırılıyor         |\n***************************************************")
elif (a==2):
    a=int(input("***************************************************\n|1.Bu Ay Kaç TL Satış Yaptınız                    |"))
    maas=baz+(a*prim/100)
    print("|Bu Ay ki Maaşınız [{}]TL`dir.İyi Çalışmalar..|\n***************************************************".format(maas))








