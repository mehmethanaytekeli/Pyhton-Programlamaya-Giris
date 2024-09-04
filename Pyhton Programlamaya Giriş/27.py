first=int(input("Enter first number: "))
secondary=int(input("Enter second number: "))
deger=1
first_=[]
secondary_=[]
ortak=0
def ekok (first,secondary,deger,ortak):
    while (1):
        first_.append(deger*first)
        secondary_.append(deger*secondary)
        deger+=1
        ortak=list(set(first_) & set(secondary_))
        if (len(ortak)==1):
            return "Bu iki sayının ekoku:",ortak[0]
print(ekok(first,secondary,deger,ortak))