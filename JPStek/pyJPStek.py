class Cvor:
    # Klasa Čvor - osnovni gradivni element za sve strukture podataka
    # Iniciranje prošireno sa parametrom sljedeci
    def __init__(self, element=None, sljedeci = None):
        self.element = element
        self.sljedeci = sljedeci
    
    def __str__(self):
        return str(self.element)

class JPStek():
    # Klasa kojom definiramo strukturu JP Steka, pomoću strukture Čvor
    # Kapacitet :: "NEOGRANIČEN"   

    # Iniciranje steka
    def __init__(self):
        self.vrh = None
        self.velicina = 0 # Već imamo metodu duzina, pa je nemoguće da nam varijabla ima isti naziv (duzina = velicina)
  
    # Ispistuje da li je stek PRAZAN (true - prazan)
    def jeLiPrazan(self):
        return self.vrh == None    

    # Vraća trenutnu dužinu(velicinu) steka tj. broj elemenata koji se nalazi u steku
    def duzina(self):
        return self.velicina

    # Dodavanje elemenata u stek
    def dodajNaStek(self,x):
        novicvor = Cvor(x, self.vrh) # Kreiranje novog cvora, sljedeći pamti podatka o čvoru koji sadrži vrijednost koja se nalazi "ispod" novog čvora
        self.vrh = novicvor          # Svaki novokreirani čvor je vrh
        self.velicina += 1
        print("Element vrijednosti " + str(x) + " je dodan na stek.")

    # Uklanjanje elemenata sa stek (LIFO)
    def ukloniSaSteka(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za uklanjanje.")
        else:            
            x = self.vrh.element                # Pamtimo vrijednost koju brisemo kako bi istu ispisali
            privremeni = self.vrh.sljedeci      # Pamtimo "sljedeći"  
            del self.vrh                        # Brišemo element na vrhu
            self.vrh = privremeni               # Novi vrh je sljedeći koji smo zapamtili
            self.velicina -= 1                  # Veličinu/Dužinu steka moramo smanjiti za 1
            print("Element vrijednosti " + str(x) + " je skinut na stek.")
    
    # U potpunosti briše stek
    def brisi(self):
        while(not (self.jeLiPrazan())):
            self.ukloniSaSteka()
        print("Stek u potpunosti obrisan!")

    # Ispis elementa na vrhu steka
    def elementNaVrhu(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za ispis.")
        else:
            print("Element na vrhu steka: " + str(self.vrh))
   
    # Ispis sadržaja steka
    def prikazi(self):
        if(self.jeLiPrazan()):
            print("Stek je prazan! Nema elemenata za ispis.")
        else:
            privremeni = self.vrh

            print("Sadržaj steka:\n")
            while(privremeni != None):
                print(str(privremeni.element))
                privremeni = privremeni.sljedeci

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
            temp = self.vrh
            self.vrh = None
            while(temp != None): 
                #self.dodajNaStek(temp)
                novicvor = Cvor(temp, self.vrh)
                self.vrh = novicvor         
                #self.velicina += 1
                temp = temp.sljedeci
            print("Poredak elemenata u steku je obrnut!")