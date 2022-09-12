import ctypes

class NizStek():
   
    # Metoda kreira niz kapaciteta k -- ctypes --za dodatni info pogledati pyNizListe
    def kreiraj_niz(self, k):
        return (ctypes.py_object * k)()

    # Iniciranje steka
    def __init__(self, kapacitet):
        self.kapacitet = kapacitet
        self.vrh = -1
        self.Niz = self.kreiraj_niz(self.kapacitet)

    # U potpunosti briše stek
    def brisi(self):
        self.vrh = -1
        print("Stek u potpunosti obrisan!")

    # Ispistuje da li je stek PRAZAN (true - prazan)
    def jeLiPrazan(self):
        return self.vrh == -1
    
    # Ispistuje da li je stek PUN  (true - pun)
    def jeLiPun(self):
        return self.vrh == self.kapacitet-1

    # Vraća trenutnu dužinu steka tj. broj elemenata koji se nalazi u steku
    def duzina(self):
        return self.vrh + 1

    # Dodavanje elemenata u stek (LIFO)
    def dodajNaStek(self,x):
        if(self.jeLiPun()):
            print("Stek je pun! Nemoguće je dodatni nove elemente.")
        else:
            self.vrh += 1
            self.Niz[self.vrh] = x
            print("Element vrijednosti " + str(x) + " je dodan na stek.")

    # Uklanjanje elemenata sa stek (LIFO)
    def ukloniSaSteka(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za uklanjanje.")
        else:
            self.vrh -= 1
            print("Element vrijednosti " + str(self.Niz[self.vrh+1]) + " je skinut na stek.") # Moguće ispisati vrijednost Niz[self.vrh+1] jer element i dalje ostaje u memoriji

    # Ispis elementa na vrhu steka
    def elementNaVrhu(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za ispis.")
        else:
            print("Element na vrhu steka: " + str(self.Niz[self.vrh]))
   
    # Ispis sadržaja steka
    def prikazi(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za ispis.")
        else:
            print("Sadržaj steka:\n")
            for i in range(self.vrh,-1,-1):
                print(str(i) + " : " + str(self.Niz[i]))
                i += 1

# UNZE PTF ASP 2021/2022 :: M.S. :: 01.12.2021

    def SkiniSaStekaVise(self, k):
        if(self.duzina() < k or k <= 0):
            print("Nemoguce skinuti toliko elemenata!")
        else:
            temp = k
            while(k != 0):
                self.ukloniSaSteka()
                k -= 1
            print("Skinuli ste ukupno: " + str(temp) + " elemenata sa steka!")

    def ObrniPoredak(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za obrtanje.")
        else:
            temp = self.kreiraj_niz(self.kapacitet)
            for i in range(self.vrh,-1,-1):
                temp[i] = self.Niz[self.vrh-i]
                i -= 1
            self.Niz = temp
            print("Elementi u steku su obrnuti!")

    def resetujStek(self):
        if(self.jeLiPun()):
            for i in range(self.kapacitet):
                self.Niz[i] = 1
        else:
            self.brisi()
            for i in range(self.kapacitet):
                self.dodajNaStek(1)
        print("Stek popunjen sa elementom 1.")
    
    def popuniPrazan(self):
        if(self.jeLiPrazan()):
            for i in range(self.kapacitet):
                self.dodajNaStek(0)
            print("Stek popunjen sa elementom 0.")
        else:
            print("Stek nije prazan!")

    def popuniPun(self):
        if(self.jeLiPun()):
            for i in range(self.kapacitet):
                self.Niz[i] = "PUNSTEK"
            print("Stek popunjen sa elementom PUNSTEK.")
        else:
            print("Stek nije pun!")