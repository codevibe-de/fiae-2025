from zipp.glob import separate


class produkt():
    def __init__(self,name,price,lager):
        self.name=name
        self.price=price
        self.lager=lager

class Warenkorb(produkt):
    def __init__(self, name, price, lager,menge: int):
        super().__init__(name, price, lager)
        self.menge=menge
    # def __init__(self,name,price,lager,menge):
    #     super().__init__(name,price,lager)
    #     self.menge=menge
    def lager_berechnung(self):
        self.lager-=self.menge
        return self.lager


class Bestellung():
    def __init__(self,*warenkorb:Warenkorb):
        self.gesamt_preis:float = 0
        self.waren:list = []
        for i in warenkorb:
            self.waren.append(i)
            self.gesamt_preis+=(i.menge*i.price)

    def namentest(self):
        for i in self.waren:
            print(i.name)




class Kunde():
    def __init__(self,vorname,name,adresse,hausnr,kreditkarte):
        self.bestellt:list = []
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

        return f"Kunde: {self.vorname}, {self.nachname} hat folgendes bestellt: {' '.join(self.bestellt)}"

    def lieferadresse(self):
        return f"{self.adresse}. {self.hausnr}"











kunde_1=Kunde("dennis","bogdanski","Straße",1,"DE9500015436854")
warenkorb_1=Warenkorb("Buch",14.50,18,6)
warenkorb_2=Warenkorb("Flasche",5.0,32,12)
bestellung_1=Bestellung(warenkorb_1,warenkorb_2)
bestellung_2=Bestellung(warenkorb_1,warenkorb_1,warenkorb_2)
print(kunde_1.bestell_history(bestellung_1,bestellung_2))





