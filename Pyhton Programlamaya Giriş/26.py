first=int(input("First Enter a number: "))
secondary=int(input("Secondary Enter a number: "))
kucuk_deger=0
if(first<secondary):
    kucuk_deger=first
else:
    kucuk_deger=secondary
def ebob(kucuk_deger,first,secondary):
    for i in range(kucuk_deger,1,-1):
        if(first % i ==0 and secondary % i == 0):
            return ("bu iki sayını ebobu :",i)
            break

print(ebob(kucuk_deger,first,secondary))
