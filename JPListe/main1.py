import pyJPListe

# Prikaz izbornika i izbor prve vrijednosti
print("     ** TESTNI PROGRAM ZA pyJPListe **")
print("-------------------Menu--------------------")
print("1. Idi na prethodni")
print("2. Idi na sljedeći")
print("3. Idi na početak")
print("4. Idi na kraj")
print("5. Idi na poziciju")
print("6. Dodavanje elementa na kraj liste")
print("7. Umetanje elementa na tekuću poziciju")
print("8. Izbacivanje tekućeg elementa")
print("9. Ispis vrijednost tekućeg elementa")
print("10. Prikaži sadržaj liste")
print("*"*30)
print("11. Trazi element")
print("12. Obrni poredak")
print("13. Obrni poredak od M do N")
print("14. Broj ponavljanja elementa")
print("15. Aritmeticka sredina")
print("16. Brisi duplikate")
print("17. Nadji maksimalni element")
print("18. Izbaci maksimalni element")
print("99. Izlaz")
unos_izbora = input("------------Izaberite opciju?-------------\n")
izbor = int(unos_izbora)

# Iniciranje objekta Liste sa kapacitetom k
# k = 10 --> Kapacitet JP Lista je "neograničen"
Lista = pyJPListe.JPlista()

# Definicija logike izbornika za pojedine funkcije strukture
def menu(izbor):
    match izbor:
        case 1:
            Lista.idiNaPrethodni()
        case 2:
            Lista.idiNaSljedeci()
        case 3:
            Lista.idiNaPocetak()
        case 4:
            Lista.idiNaKraj()
        case 5:
            pozicija = input("Unesite poziciju za dislokaciju pokazivača tekući!\n")
            Lista.idiNaPoziciju(int(pozicija))
        case 6:
            x = int(input("Unesite vrijednost elementa!\n"))
            Lista.dodaj(x)
        case 7:
            x = int(input("Unesite vrijednost elementa!\n"))
            Lista.umetni(x)
        case 8:
            Lista.izbaci()
        case 9:
            Lista.ispisiTekuci()
        case 10:
            print("** ELEMENTI U LISTI **")
            Lista.prikazi()
        case 11:
            t = int(input("Unesite element za pretragu: "))
            Lista.trazi(t)
        case 12:
            Lista.obrniPoredak()
        case 13:
            m = int(input("Unesite vrijednost M: "))
            n = int(input("Unesite vrijednost N: "))
            Lista.obrniPoredakodMdoN(m,n)
        case 14:
            p = int(input("Unesite element za pretragu: "))
            Lista.brojPonavljanja(p)
        case 15:
            Lista.aritmetickaSredina()
        case 16:
            Lista.brisiDuplikate()
        case 17:
            Lista.NadjiMax()
        case 18:
            Lista.IzbaciMax()
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")

# Petlja za ponavlejnje izbora do unosa izlaza
while (izbor):    
    menu(izbor)
    unos_izbora = input("------------Izaberite opciju?-------------\n")
    izbor = int(unos_izbora)
