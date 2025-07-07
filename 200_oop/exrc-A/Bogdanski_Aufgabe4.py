
class produkt():
    name:str
    price:float
    lager:int
    def __init__(self,name,price,lager):
        self.name=name
        self.price=price
        self.lager=lager

class Warenkorb(produkt):
    menge:int
    def __init__(self,produkt:produkt,menge:int):
        self.name=produkt.name
        self.price=produkt.price
        self.lager=produkt.lager
        self.menge=menge
    # def __init__(self,name,price,lager,menge):
    #     super().__init__(name,price,lager)
    #     self.menge=menge
    def lager_berechnung(self):
        self.lager=self.lager-self.menge
        return self.lager


class Bestellung():
    gesamt_preis:float = 0
    waren=[]
    def __init__(self,*warenkorb:Warenkorb):
        for i in warenkorb:
            self.waren.append(i)
            self.gesamt_preis=self.gesamt_preis+(i.menge*i.price)

    def namentest(self):
        for i in self.waren:
            print(i.name)



class Kunde():
    vorname:str
    nachname:str
    adresse:str
    hausnr:int
    kreditkarte:str
    bestellt=[]
    def __init__(self,vorname,name,adresse,hausnr,kreditkarte):
        self.vorname=vorname
        self.nachname=name
        self.hausnr=hausnr
        self.adresse=adresse
        self.kreditkarte=kreditkarte

    def bestell_history(self,*bestellung:Bestellung):
        for i in bestellung:
            self.bestellt.append("| Bestellung:")
            for x in i.waren:
                historie=(f"{x.name} Menge: {x.menge}")
                self.bestellt.append(historie)
            self.bestellt.append(f"für Gesamt: {i.gesamt_preis}€ |")

        return f"Kunde: {self.vorname}, {self.nachname} hat folgendes bestellt: {self.bestellt}"










kunde_1=Kunde("dennis","bogdanski","straße",1,"DE9500015436854")
produkt_1=produkt("Buch",14.50,12)
produkt_2=produkt("Flasche",5.0,25)
warenkorb_1=Warenkorb(produkt_1,6)
warenkorb_2=Warenkorb(produkt_1,2)
warenkorb_3=Warenkorb(produkt_2,7)
bestellung_1=Bestellung(warenkorb_1,warenkorb_2)
bestellung_2=Bestellung(warenkorb_1,warenkorb_3)
print(kunde_1.bestell_history(bestellung_2,bestellung_1))



