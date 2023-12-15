a=0
b=0
c=0
d=0
f=0
d=int(input("kaç tane sayıyı toplamak istersiniz:"))
f=int(input("toplam kaç olunca kod sonlancak:"))

for i in range (d):
    a=int(input("{}. sayı giriniz:".format(c+1)))
    a+=b
    c += 1

if(c==d):
     if(b>f):
        print("Başarısız")
     else:
        print("Başarılı")
