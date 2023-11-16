yıldız=int(input("Kac Tane Yıldız Olsun?"))
a=0
def yıldız_fak(yıldız):
    for a in range(1,yıldız,2):
        bosluk=int((100-a)/2)
        print(" "*bosluk,"*"*a)
yıldız_fak(yıldız)