degisken2=0
degisken1=0
degisken3=16000
while 1:
    saat=int(input("kaç saat çalıştınız bu hafta?"))
    if saat<1:
        print("yanlış değer girildi kod sonlandırılıyor...")
        break
    else:
        if saat<40:
            saat=saat*400
            print(saat,"tl kazandınız bu hafta")
        else:
            degisken2= saat - 40
            degisken1= degisken2 * 600
            saat= degisken1 + degisken3
            print(saat,"tl kazandınız bu hafta")