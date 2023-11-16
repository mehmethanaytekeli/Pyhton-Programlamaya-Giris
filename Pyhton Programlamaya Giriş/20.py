sayı=int(input("Kacıncı Sayının Fibonanci Serisini Hesaplama İstersiniz?"))
def fibo(sayı):
    if(sayı==1 or sayı==2):
        return 1
    else:
        return  fibo(sayı-1) + fibo(sayı-2)
print(fibo(sayı))