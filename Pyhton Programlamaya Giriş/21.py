while(1):
    saniye=int(input("******************\nSaniyeyi giriniz:\n******************"))
    gün=int(saniye/84600)
    günkalan=saniye%84600
    saat=int(günkalan/3600)
    saatkalan=günkalan%3600
    dakika=int(saatkalan/60)
    if(gün<1):
        print(saniye," saniye",saat,"saate",dakika,"dakikaya esittir")
    elif(saat<1):
        print(saniye,"saniye",dakika,"dakikaya esittir")
    else:
        print(saniye," saniye",gün,"Güne",saat,"saate",dakika,"dakikaya esittir")


#this code by mehmethan aytekeli