a=0
b=50
for a in range(1,100,2):
    print("\n")

    while(a):
        print(" "*b,"*"*a,end=" ")
        a -=a
        b -=1
