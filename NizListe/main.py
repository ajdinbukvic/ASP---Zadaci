
import pyNizListe

# Prikaz izbornika
print("      ** TESTNI PROGRAM ZA pyListe **")
print("-------------------Menu--------------------")
print("1. Idi na početak")
print("2. idi na kraj")
print("3. Idi na prethodni")
print("4. Idi na sljedeći")
print("5. Idi na poziciju")
print("6. Dodavanje elemenata na kraj liste")
print("7. Umetanje elmenta na tekuću poziciju")
print("8. Izbacivanje tekućeg elementa")
print("9. Ispis vrijednosti tekućeg elementa")
print("10. Prikaz sadržaja liste")
print("11. Izbaci minimalni element")
print("12. Zamijeni min i max")
print("13. Dodaj ASredinu u sredinu ili pocetak")
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Iniciranje objekata Liste sa kapacitetom k
k = 10
Lista = pyNizListe.NizLista(k)

# Funkcija izbornika
def menu(izbor):
    match izbor:
        case 1:
            Lista.idiNaPocetak()
        case 2:
            Lista.idiNaKraj()
        case 3:
            Lista.idiNaPrethodni()
        case 4:
            Lista.idiNaSljedeci()
        case 5:
            pozicija = input("Unesite poziciju za dislokaciju pokazivača tekući!\n")
            Lista.idiNaPoziciju(int(pozicija))
        case 6:
            x = input("Unesite vrijednost elementa!\n")
            Lista.dodaj(x)
        case 7:
            x = input("Unesite vrijednost elementa!\n")
            Lista.umetni(x)
        case 8:
            Lista.izbaci()
        case 9:
            Lista.ispisiTekuci()
        case 10:
            print("** ELEMENTI U LISTI **")
            Lista.prikazi()
        case 11:
            Lista.izbaciMin()
        case 12:
            Lista.ZamijeniMinMax()
        case 13:
            Lista.dodajASUSredinu()
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")

# Petlja, while, dok god postoji unos izbora
while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)

# UNZE PTF ASP 2021/2022 :: M.S. :: 10.11.2021