a = input("İki basamaklı bir sayı girin: ")

def onlar(a):
    match a[0]:
        case '1':
            return "On"
        case '2':
            return "Yirmi"
        case '3':
            return "Otuz"
        case '4':
            return "Kırk"
        case '5':
            return "Elli"
        case '6':
            return "Altmış"
        case '7':
            return "Yetmiş"
        case '8':
            return "Seksen"
        case '9':
            return "Doksan"

def birler(a):
    match a[1]:
        case '1':
            return "Bir"
        case '2':
            return "İki"
        case '3':
            return "Üç"
        case '4':
            return "Dört"
        case '5':
            return "Beş"
        case '6':
            return "Altı"
        case '7':
            return "Yedi"
        case '8':
            return "Sekiz"
        case '9':
            return "Dokuz"

print(onlar(a), birler(a))
