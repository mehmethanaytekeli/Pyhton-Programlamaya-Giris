birinci=int(input("Birinci Sayıyı Giriniz:"))
ikinci=int(input("İkinci Sayıyı Giriniz:"))
islem=int(input("Hangi İşlemi Seçmek istersiniz?\n1.Toplama\n2.Cıkarma\n3.Carpma\n4.Bölme\n"))
def topla(birinci,ikinci):
    return birinci+ikinci
def cıkar(birinci,ikinci):
    return birinci-ikinci
def carp(birinci,ikinci):
    return birinci*ikinci
def bol(birinci,ikinci):
    bolum=birinci/ikinci
    return bolum
if(islem==1):
    print(topla(birinci,ikinci))
elif(islem==2):
    print(cıkar(birinci,ikinci))
elif (islem == 3):
    print(carp(birinci, ikinci))
elif (islem == 4):
    print(f"{bol(birinci, ikinci):.1f}")
else:
    print("Yanlış Değer Girdiniz... ")