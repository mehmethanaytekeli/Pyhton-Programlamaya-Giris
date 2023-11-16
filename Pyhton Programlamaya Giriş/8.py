a=0
b=0
c=0
for i in range (5):
    a=int(input("{}. sayı giriniz".format(c+1)))
    a+=b
    c += 1

if(c==5):
    if(b<100):
        print("Başarısız")
    else:
        print("Başarılı")
