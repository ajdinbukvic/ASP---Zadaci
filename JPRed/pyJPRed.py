class Cvor:
    # Klasa Čvor - osnovni gradivni element za sve strukture podataka
    # Iniciranje prošireno sa parametrom sljedeci
    def __init__(self, element=None, sljedeci = None):
        self.element = element
        self.sljedeci = sljedeci
    
    def __str__(self):
        return str(self.element)

class JPRed():
    # Klasa kojom definiramo strukturu JP Red, pomoću strukture Čvor
    # Kapacitet :: "NEOGRANIČEN"   

    # Iniciranje reda
    def __init__(self):
        self.pocetak = None
        self.kraj = None
        self.velicina = 0 # Već imamo metodu duzina, pa je nemoguće da nam varijabla ima isti naziv (duzina = velicina)

    # Ispistuje da li je red PRAZAN (true - prazan)
    def jeLiPrazan(self):
        return self.pocetak == None

    # Vraća trenutnu dužinu reda tj. broj elemenata koji se nalazi u redu
    def duzina(self):
        return self.velicina

    # Dodavanje elemenata u red
    def dodajURed(self,x):
        novicvor = Cvor(x)                # Kreiranje novog cvora
        
        if(self.pocetak == None):                   # Ako je red prazan
            self.pocetak = self.kraj = novicvor 
        else:
            self.kraj.sljedeci = novicvor           # Povezujemo element na kraju sa novim cvorom
            self.kraj = self.kraj.sljedeci          # Pokazivač kraj prebacujemo na novi cvor

        self.velicina += 1
        print("Element vrijednosti " + str(x) + " je dodan u red.")

    # Izbacivanje elemenata iz rada (FIFO)
    def izbaciIzReda(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za izbacivanje!")
        else:
            x = self.pocetak.element                    # Pamtimo vrijednost koju brisemo kako bi istu ispisali
            privremeni = self.pocetak            

            if (self.pocetak == self.kraj):             # Samo jedan element u redu
                self.pocetak = self.kraj = None         # Prazan red
            else:
                self.pocetak = self.pocetak.sljedeci    # Pomjeramo pokazivač početak na element koji se nalazi iza u redu
            
            del privremeni                              # Brišemo element iz memorije            
            self.velicina -= 1                          # Veličinu/Dužinu reda moramo smanjiti za 1
            print("Element vrijednosti " + str(x) + " je uklonjen iz reda.")

    # U potpunosti briše red
    def brisi(self):
        while(not (self.jeLiPrazan())):
            self.izbaciIzReda()
        print("Red u potpunosti obrisan!")

    # Ispis elementa na vrpoečtku reda
    def elementNaCelu(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za ispis.")
        else:
            print("Element na početku reda: " + str(self.pocetak))
   
    # Ispis sadržaja reda
    def prikazi(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za ispis.")
        else:
            print("Sadržaj reda:\n")

            privremeni = self.pocetak

            while(privremeni != None):
                print(str(privremeni.element))
                privremeni = privremeni.sljedeci        

# UNZE PTF ASP 2021/2022 :: M.S. :: 01.12.2021

    def minElement(self):
        if(self.jeLiPrazan()):
            print("Red je prazan! Nema elemenata za poredjenje.")
        else:
            min = self.pocetak
            temp = self.pocetak.sljedeci
            while(temp != None):
                if(int(temp.element) < int(min.element)):
                    min = temp
                temp = temp.sljedeci
            print("Vrijednost minimalnog elementa je: " + str(min.element))