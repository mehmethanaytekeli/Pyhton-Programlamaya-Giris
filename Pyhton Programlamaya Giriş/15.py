from random import randrange
a=randrange(0,100)
c=0
while(1):
    b=int(input("Hangi Sayıy Tutmuş Olabilirim?"))
    c =c+1
    if(a<b):
        print("Biraz Daha Aşağıda Gibi Hissediyorum :)")
    elif(b<a):
        print("Biraz Daha Yukarıda Gibi Hissediyorum :)")
    else:
        print("Sonunda {}.Hamlede Bulabildiniz".format(c))
        break




