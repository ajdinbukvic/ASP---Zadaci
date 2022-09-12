# *** JEDNOSTRUKO POVEZANE LISTE ***

class Cvor:
    # Klasa Čvor - osnovni gradivni element za sve strukture podataka
    def __init__(self, element=None):
        self.element = element
        self.sljedeci = None
    
    def __str__(self):
        return str(self.element)

class JPlista():
    # Klasa kojom definiramo strukturu JP Lista, pomoću strukture Čvor
    # Kapacitet :: "NEOGRANIČEN"
    def __init__(self):
        self.pocetak = None
        self.kraj = None
        self.tekuci = None
        self.dduzina = 0
        self.lduzina = 0
    
    # Pozicioniranje na početak
    def idiNaPocetak(self):
        self.tekuci = self.pocetak
        self.dduzina += self.lduzina
        self.lduzina = 0
        print("Pokazivač tekući postavljen na POČETAK liste!")
    
    # Pozicioniranje na kraj
    def idiNaKraj(self):
        self.tekuci = self.kraj
        self.lduzina += self.dduzina
        self.dduzina = 0
        print("Pokazivač tekući postavljen na KRAJ liste!")

    # Pozicioniranje na sljedeći
    def idiNaSljedeci(self):
        if(self.dduzina != 0):
            if(self.tekuci == None): # Tekući nije postavlje!
                self.tekuci = self.pocetak
                print("Pokazivač je postavljen an POČETAK liste!")
            else:
                self.tekuci = self.tekuci.sljedeci
            self.lduzina += 1
            self.dduzina -= 1
            print("Pokazivač tekući postavljen na SLJEDEĆI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na kraju liste!")

    # Pozicioniranje na prethodni
    def idiNaPrethodni(self):
        if(self.lduzina != 0):
            if(self.lduzina == 1):
                self.tekuci = self.pocetak
                print("Pokazivač je postavljen na POČETAK liste!")
            else:
                privremeni = self.pocetak
                while(privremeni.sljedeci != self.tekuci):
                    privremeni = privremeni.sljedeci
                self.tekuci = privremeni
                print("Pokazivač tekući je postavljen na PRETHODNI ELEMENT liste!")
            self.lduzina -= 1
            self.dduzina += 1
        else:
            print("Pokazivač tekući je na početku liste!")

    # Pozicioniranje na proizvoljnu poziciju (lijevo)
    def idiNaPoziciju(self, pozicija):
        if((pozicija < 0) or (pozicija > (self.lduzina + self.dduzina))):
            print("Zadata pozicija je izvan raspona!")
        else:
            self.dduzina = self.dduzina + self.lduzina - pozicija
            self.lduzina = pozicija
            if(pozicija == 0):
                #self.tekuci = self.pocetak
                self.tekuci = None #IZMJENA
                print("Pokazivač tekući pokazuje na POČETAK liste")
            else:
                self.tekuci = self.pocetak
                for i in range(0,pozicija-1):
                    self.tekuci = self.tekuci.sljedeci
            #print("Pokazivač tekući postavljen na poziciju:" + str(pozicija))
                print("Pokazivač tekući postavljen na poziciju:" + str(pozicija)) #IZMJENA

    # Dodavanje elemenata na kraj
    def dodaj(self, x):
        novicvor = Cvor(x)
        
        if(self.dduzina+self.lduzina == 0):     # Ukoliko je JL Lista prazna
            self.pocetak = novicvor
            self.kraj = novicvor
            print("Lista je bila prazna. Početak i kraj liste su sada isti novi čvor!")
        else:                                   # Ukoliko JP Lista nije prazna
            self.kraj.sljedeci = novicvor       # Trenutnom cvoru na karjau se popunjava pokazivać sljedeći na novi čvor
            self.kraj = novicvor                # Pokazivač kraj se pomjera na novi čvor na kraju liste
            print("Uspješno dodan element na kraj liste!")
        
        self.dduzina += 1

    # Umetanje elmenta na tekuću poziciju (dodatni element na desnoj particiji)
    def umetni(self, x):
        privremin = Cvor(x)

        if (self.lduzina == 0):
            privremin.sljedeci = self.pocetak
            self.pocetak = privremin
            #self.tekuci = privremin
            if(self.lduzina+self.dduzina == 0):
                self.kraj = privremin
            print("Uspješno umetnut element " + str(x) + " na početak liste")
        else:
            privremin.sljedeci = self.tekuci.sljedeci
            self.tekuci.sljedeci = privremin
            if(self.dduzina == 0):
                self.kraj = self.tekuci.sljedeci #privremeni
            print("Uspješno umetnut element " + str(x) + " na poziciju pokazivača " + str(self.tekuci))
        
        self.dduzina += 1    

    # Izabcivanje/Brisanje tekućeg elementa - prvog elementa desne particije
    def izbaci(self):
        if (self.dduzina <= 0):
            print("Nema elemenata za izbacivanje/brisanje! Tekući na kraju liste!")
        else: #IZMJENA - dodan else a dio ispod uvucen za jedan tab
            privremen = Cvor()
        
            if(self.lduzina == 0):                          # Tekući na početku liste
                privremin = self.pocetak
                self.pocetak = privremin.sljedeci
                print("Izvršeno je izbacivanje elementa!")
            else:
                privremen = self.tekuci.sljedeci             # Tekući u sredini liste
                self.tekuci.sljedeci = privremen.sljedeci
                print("izvršeno je izbacivanje elementa!")
        
            if(self.dduzina == 1):                          # Tekući na jedan element prije kraja liste
                self.kraj = self.tekuci
        
            self.dduzina -= 1

    # Ispis tekućeg elementa (lijevo)
    def ispisiTekuci(self):
        if (self.dduzina == 0):
            print("Nema elemnata za ispis! Pokazivač je na kraju liste!")
        elif(self.tekuci == None):
            print("Vrijednost elementa na početku liste je: " + str(self.pocetak.element))
        else:
            print("Vrijednost elementa na tekućoj poziciji je: " + str(self.tekuci.element))

    # Prikazivanje/Ispis svih elemenata liste
    def prikazi(self):
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna!")
        else:
            privremeni = self.pocetak
            brojac = 0

            while(privremeni != None):
                print(str(brojac) + ": " + str(privremeni), end="")

                # Dopunski pokazivači na ispisu
                if (privremeni == self.pocetak):
                    print( " <- početak",end="")
                if(privremeni == self.tekuci):
                    print( " <- tekući",end="")
                if(privremeni == self.kraj):
                    print( " <- kraj",end="")
                print("")

                privremeni = privremeni.sljedeci
                brojac += 1

    def ASredinaTrecina(self):
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna!")
        else:
            suma = 0
            temp = self.pocetak
            while(temp != None):
                suma += int(temp.element)
                temp = temp.sljedeci
            asredina = float(suma/(self.dduzina+self.lduzina))
            trecina = float(asredina/3)
            print("Trecina ASredine je: " + str(trecina))
    
    def DodajUSredinu(self):
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna!")
        else:
            suma = 0
            temp = self.pocetak
            while(temp != None):
                suma += int(temp.element)
                temp = temp.sljedeci
            if((self.dduzina+self.lduzina) % 2 == 0):
                polovina = int((self.dduzina+self.lduzina)/2)
                self.idiNaPoziciju(polovina)
                self.umetni(suma)
                print("Dodali ste sumu u sredinu liste!")
            else:
                self.dodaj(suma)
                print("Dodali ste sumu na kraj liste!")