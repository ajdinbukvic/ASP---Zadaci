# Python u osnovnoj biblioteci ne podržava tip podataka array
# Postoji biblioteka array --> from array import *
# Koja podrazumijeva homogenost strukture i ugrađene funcije za rad sa nizovima, što za našu customiziranu strukturu nije slučaj korištenja kao što to nisu ni pyListe
# Za rad sa array tipom podataka neophodno koristiti dodatnu biblioteku ctypes ili numpy
import ctypes
# import numpy as np - https://numpy.org/doc/stable/reference/generated/numpy.array.html
# biblioteka numpy ima ugrađene i već funkcije koje omogućavaju operacije sa nizovima uz proširenja i olakšice kao što su prazni nizovi, povećanje kapaciteta, što za našu customiziranu strukturu nije slučaj korištenja ....


class NizLista():
    # Klasa kojom se definira struktura podataka Lista, pomoću nizova(array), koja je
    # konačna - rezervirana i ograničena memorija/veličina liste
    # homogena - isti tip objekata

    def kreiraj_niz(self, k):
        return (ctypes.py_object * k)()
    # Kreira niz kapaciteta k
    # ctypes documentation : https://docs.python.org/3/library/ctypes.html#arrays
    # class ctypes.py_object - Represents the C PyObject* datatype. Calling this without an argument creates a NULL PyObject* pointer.

    # Iniciranje liste sa predodređenim kapacitetom
    def __init__(self, kapacitet):
        self.kapacitet = kapacitet
        self.duzina = 0
        self.tekuci = 0
        self.Niz = self.kreiraj_niz(self.kapacitet)
    
    # Pozicioniranje na početak
    def idiNaPocetak(self):
        self.tekuci = 0
        print("Pokazivač tekući postavljen na POČETAK liste!")
    
    # Pozicioniranje na kraj
    def idiNaKraj(self):
        self.tekuci = self.duzina
        print("Pokazivač tekući postavljen na KRAJ liste!")

    # Pozicioniranje na sljedeći
    def idiNaSljedeci(self):
        if(self.tekuci < self.duzina):
            self.tekuci += 1
            print("Pokazivač tekući postavljen na SLJEDEĆI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na kraju liste!")

    # Pozicioniranje na prethodni
    def idiNaPrethodni(self):
        if(self.tekuci != 0):
            self.tekuci -= 1
            print("Pokazivač tekući postavljen na PRETHODNI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na početku liste!")

    # Pozicioniranje na proizvoljnu poziciju
    def idiNaPoziciju(self, pozicija):
        if((pozicija < 0) or (pozicija > self.duzina)):
            print("Zadata poziciaj je izvan raspona!")
        else:
            self.tekuci = pozicija
            print("Pokazivač tekući postavljen na poziciju:" + str(pozicija))

    # Dodavanje elementa na kraj liste
    def dodaj(self,x):
        if(self.duzina < self.kapacitet):
            self.Niz[self.duzina] = x
            self.duzina += 1
            print("Uspješno dodan element!")
        else:
            print("Kapacitet popunjen!")

    # Dužina lijeve particije
    def lDuzina(self):
        return self.tekuci

    # Dužina desne particije
    def dDuzina(self):
        return self.duzina - self.tekuci
    
    # Umetanje lementa na tekuću poziciju
    def umetni(self, x):
        if(self.duzina < self.kapacitet):
            for i in range(self.duzina,self.tekuci,-1): # Elemente od kraja niza do tekućeg pokazivača
                self.Niz[i] = self.Niz[i-1]             # pomjera za jedno mjesto u desno
            self.Niz[self.tekuci] = x
            self.duzina += 1
            print("Uspješno umetnut element " + str(x) + " na poziciju pokazivača " + str(self.tekuci))
        else:
            print("Kapacitet popunjen!")

    # Izabcivanje/Brisanje tekućeg elementa - vrijednost elementa sa desne strane od indeksa pokazivača tekući
    def izbaci(self):
        if (self.dDuzina() <= 0):
            print("nema elemenata za izbacivanje/brisanje! Tekući na kraju liste!")
        else:
            izbacei = self.Niz[self.tekuci]
            for i in range (self.tekuci,self.duzina-1): # Elemente od tekućeg pokazivača do kraja niza 
                self.Niz[i] = self.Niz[i+1]             # pomjera za jedno mjesto u lijevo
            self.duzina -= 1
            print("izvršeno je izbacivanje elementa vrijednosti: " + str(izbacei))

    # Ispis tekućeg elementa
    def ispisiTekuci(self):
        if (self.dDuzina() <= 0):
            print("Nema elemnata za ispis! Pokazivač je na kraju liste!")
        else:
            print("Vrijednost elementa na tekućoj poziciji je: " + str(self.Niz[self.tekuci]))
    
    # Prikazivanje/Ispis svih elemenata liste
    def prikazi(self):
        print("Kapacitet liste:" + str(self.kapacitet))
        print("Dužina liste:" + str(self.duzina))
        #py doc --> range(start, stop, step)
        for i in range(0,self.duzina):
            print("Element " + str(i+1) + " - pozicija(" + str(i) + "): " + str(self.Niz[i]))

# UNZE PTF ASP 2021/2022 :: M.S. :: 10.11.2021
    def povecajKapacitet(self, k):
        if(k <= self.kapacitet):
            print("Novi kapacitet ne moze biti manji ili jednak starom kapacitetu!")
        else:
            temp = self.kreiraj_niz(k) 
            for i in range(self.duzina): 
                temp[i] = self.Niz[i]
            self.Niz = temp 
            self.kapacitet = k

    def obrniPoredak(self):
        dd = self.dDuzina()
        temp = self.kreiraj_niz(self.duzina)
        d = self.duzina - 1
        for i in range(self.duzina):
           temp[d] = self.Niz[i]
           d -= 1
        self.Niz = temp
        self.tekuci = dd
        print("Poredak u listi je obrnut!")

    def NadjiMinClan(self):
        temp = self.Niz[0]
        for i in range(1,self.duzina):
            if(self.Niz[i] < temp): #max self.Niz[i] > temp
                temp = self.Niz[i]
        print("Najmanji clan u nizu je: "+ str(temp))

    def NadjiMinIndex(self):
        temp = self.Niz[0]
        index = 0
        for i in range(1,self.duzina):
            if(self.Niz[i] < temp): #max self.Niz[i] > temp
                temp = self.Niz[i]
                index = i
        print("Najmanji clan u nizu je na indeksu: "+ str(index))
        return int(index)
    
    def IzbaciMin(self): #IzbaciMax
        temp = self.NadjiMinIndex()
        if(temp == self.duzina - 1):
            izbaci = self.Niz[temp]        
            self.duzina -= 1
            print("izvršeno je izbacivanje elementa vrijednosti: " + str(izbaci))
        else:
            self.tekuci = temp
            self.izbaci()
    
    def ZamjeniParticije(self):
        ld = self.lDuzina()
        dd = self.dDuzina()
        temp = self.kreiraj_niz(ld)
        for i in range(ld):
            temp[i] = self.Niz[i]
        for i in range(dd):
            self.Niz[i] = self.Niz[i+ld]
        for i in range(dd,self.duzina):
            self.Niz[i] = temp[i-dd]
        self.tekuci = dd
        print("Lijeva i desna particija liste su zamijenjene!")
    


