import ctypes

class CRed():
   
    # Metoda kreira niz kapaciteta k -- ctypes --za dodatni info pogledati pyNizListe
    def kreiraj_niz(self, k):
        return (ctypes.py_object * k)()

    # Iniciranje reda
    def __init__(self, kapacitet):
        self.kapacitet = kapacitet
        self.pocetak = -1
        self.kraj = -1
        self.Niz = self.kreiraj_niz(self.kapacitet)

    # U potpunosti briše red
    def brisi(self):
        self.pocetak = -1
        self.kraj = -1        
        print("Red u potpunosti obrisan!")

    # Ispistuje da li je red PRAZAN (true - prazan)
    def jeLiPrazan(self):
        return self.pocetak == -1
    
    # Ispistuje da li je red PUN  (true - pun)
    def jeLiPun(self):
        return self.pocetak == (self.kraj+1) % self.kapacitet

    # Vraća trenutnu dužinu reda tj. broj elemenata koji se nalazi u redu
    def duzina(self):
        if (self.pocetak == -1):
            return 0
        else:
            return ((self.kraj + self.kapacitet) - self.pocetak) % self.kapacitet + 1

    # Dodavanje elemenata u red
    def dodajURed(self,x):
        if(self.jeLiPun()):
            print("Red je pun! Nemoguće je dodatni nove elemente.")
        else:
            self.kraj = (self.kraj + 1) % self.kapacitet
            self.Niz[self.kraj] = x
            if(self.pocetak == -1):  # Ukoliko je Red bio prazan, potrebno je i promjeniti pokazivač početak
                self.pocetak = 0
            print("Element vrijednosti " + str(x) + " je dodan u red.")

    # Izbacivanje elemenata siz rada (FIFO)
    def izbaciIzReda(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za izbacivanje!")
        else:
            x = self.Niz[self.pocetak]
           
            if (self.pocetak == self.kraj):     # samo jedan element u redu
                self.pocetak = self.kraj = -1   # prazan red
            else:
                self.pocetak = (self.pocetak + 1) % self.kapacitet

            print("Element vrijednosti " + x + " je izbačen iz reda.") 

    # Ispis elementa na početku reda
    def elementNaCelu(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za ispis.")
        else:
            print("Element na početku reda: " + str(self.Niz[self.pocetak]))
   
    # Ispis sadržaja reda
    def prikazi(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za ispis.")
        else:
            print("Sadržaj reda:\n")

            i = self.pocetak
            # U pythonu ne postoji klasična do-while petlja
            while True:
                print(str(i) + " : " + str(self.Niz[i]))
                i = (i +1) % self.kapacitet

                if (i == (self.kraj + 1) % self.kapacitet):
                    break           

# UNZE PTF ASP 2021/2022 :: M.S. :: 01.12.2021

    def PolovinaASredine(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za racunanje.")
        else:
            suma = 0
            i = self.pocetak
            while True:
                suma += int(self.Niz[i])
                i = (i+1) % self.kapacitet
                if (i == (self.kraj + 1) % self.kapacitet):
                    break
            asredina = float(suma/self.duzina())
            polovina = float(asredina/2)
            print("Polovina ASredine iznosi: " + str(polovina))     

    def dodajSumu(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za racunanje.")
        else:
            suma = 0
            i = self.pocetak
            while True:
                suma += int(self.Niz[i])
                i = (i+1) % self.kapacitet
                if (i == (self.kraj + 1) % self.kapacitet):
                    break
            polovina = float(suma/2)
            print("Polovina sume iznosi: " + str(polovina))   
            self.dodajURed(polovina)

    def kvadratReda(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za racunanje.")
        else:
            suma = 0
            i = self.pocetak
            while True:
                suma += int(self.Niz[i])
                i = (i+1) % self.kapacitet
                if (i == (self.kraj + 1) % self.kapacitet):
                    break
            kvadrat = int(suma*suma)
            print("Kvadrat sume iznosi: " + str(kvadrat))   
            



