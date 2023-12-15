a=1
for a in range(1,10):
    yil=int(input("dogdugunuz yılı girin:"))
    yas=int(2023-yil)
    if(yil<2023):
        if(0<=yas<=2):
            print("Bebeksin")
        elif(3<=yas<=17):
            print("çocuksun")
        elif(18<=yas<=30):
            print("Gençsiniz")
        elif(31<=yas<=65):
            print("orta yaşlısnız")
        else:
            print("bir ayağınız çukurda")
    else:
        print("Bu yaşta doğmuş olamassınız")



