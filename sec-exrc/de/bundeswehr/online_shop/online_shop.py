# Einfaches Online-Shop-System

class Produkt:

    #Repräsentiert ein Produkt im Online-Shop.

    def __init__(self, name: str, preis: float, bestand: int):
        # Wird aufgerufen, wenn ein neues Produktobjekt erzeugt wird.
        self.name = name
        self.preis = preis
        self.bestand = bestand

    def lager_reduzieren(self, menge: int):
        # Prüft, ob genug Bestand vorhanden ist.
        if menge > self.bestand:
            raise ValueError(f"Nicht genug Bestand für {self.name}: {self.bestand} verfügbar, {menge} angefragt")
        # Ziehe die Menge vom Lagerbestand ab.
        self.bestand -= menge

    def __str__(self):
        # Definiert, wie das Objekt als String dargestellt wird.
        # Hier: Name, Preis mit 2 Nachkommastellen und aktueller Lagerbestand.
        return f"{self.name}: {self.preis:.2f}€, Lager: {self.bestand}"


class Kunde:

    #Repräsentiert einen Kunden mit Bestellhistorie.

    def __init__(self, name: str):
        self.name = name
        self.bestellungen = []  # Liste der Bestellungen // # Leere Liste, die später Bestellung-Objekte aufnimmt

    def bestellung_hinzufuegen(self, bestellung):
        self.bestellungen.append(bestellung)

    def __str__(self):
        return f"Kunde: {self.name}"


class Bestellung:

    #Repräsentiert eine abgeschlossene Bestellung.
    #Speichert was Bestellt wurde und berechnet die Summe.

    zaehler = 1  # Klassen Variable für Bestellnummern

    def __init__(self, kunde, items, rabatt_rate):
        # Speichert den Namen des Kunden für spätere Ausgabe.
        self.kundename = kunde.name
        # Speichert den Namen des Kunden für spätere Ausgabe.
        self.items = items.copy()

        # Nummer der Bestellung
        # weist dieser Bestellung eine eindeutige Nummer zu und erhöht den Zähler.
        self.nummer = Bestellung.zaehler
        Bestellung.zaehler += 1

        # Berechnungen ab 100% gibt es z.B 5% Rabatt
        self.subtotal = sum(prod.preis * qty for prod, qty in items.items())
        self.rabatt = int(rabatt_rate * 100)
        # Gesamtbetrag nach Abzug des Rabatts.
        self.total = self.subtotal * (1 - rabatt_rate)

    def __str__(self):
        # Baut eine Liste von Zeilen für die Ausgabe.
        ausgabe = [f"Bestellung {self.nummer} von {self.kundename}"]
        # Listet alle Artikel mit Menge und Einzelkosten auf.
        for prod, qty in self.items.items():
        # Fügt Zwischensumme hinzu.
            ausgabe.append(f"  - {prod.name} x{qty} = {prod.preis * qty:.2f}€")
        ausgabe.append(f"Zwischensumme: {self.subtotal:.2f}€")
        if self.rabatt > 0:
            # Nur wenn Rabatt > 0 wird er angezeigt.
            ausgabe.append(f"Rabatt: {self.rabatt}%")
            # Fügt den Endbetrag hinzu.
        ausgabe.append(f"Gesamt: {self.total:.2f}€")
        # Fügt alle Zeilen zu einem einzigen String zusammen.
        return "\n".join(ausgabe)


class Warenkorb:

    #Repräsentiert den Warenkorb eines Kunden.
    #Rabatt: 5% ab 100€ Zwischensumme.

    RABATT_SCHWELLE = 100   # Schwelle in Euro
    RABATT_RATE = 0.05      # 5% Rabatt

    def __init__(self, kunde):
        # Verknüpft den Warenkorb mit einem Kunden.
        self.kunde = kunde
        # Leeres Dict: Schlüssel = Produktobjekt, Wert = Menge.
        self.items = {}

    def produkt_hinzufuegen(self, produkt, menge=1):
        # Validiert, dass die Menge positiv ist.
        if menge <= 0:
            raise ValueError("Menge muss größer als 0 sein")
        # Reduziert den Lagerbestand und speichert die Menge.
        produkt.lager_reduzieren(menge)
        # .get(produkt, 0) liefert vorhandene Menge oder 0, danach addierte neue Menge.
        self.items[produkt] = self.items.get(produkt, 0) + menge

    def berechne_subtotal(self):
        # Summiert Preis * Menge aller Produkte.
        return sum(prod.preis * qty for prod, qty in self.items.items())

    def berechne_rabatt_rate(self):
        # Prüft, ob Subtotal >= Schwelle, und gibt Rate zurück (0 oder 0.05).
        return self.RABATT_RATE if self.berechne_subtotal() >= self.RABATT_SCHWELLE else 0

    def checkout(self):
        # Holt die anzuwendende Rabatt-Rate.
        rate = self.berechne_rabatt_rate()
        # Erstellt eine Bestellung mit allen aktuellen Items und dem Rabatt.
        bestellung = Bestellung(self.kunde, self.items, rate)
        # Speichert die Bestellung in der Kundenhistorie.
        self.kunde.bestellung_hinzufuegen(bestellung)
        # Leert den Warenkorb für eine neue Bestellung.
        self.items.clear()
        return bestellung

    def __str__(self):
        # Baut eine Ausgabeliste für den Warenkorb.
        ausgabe = ["Warenkorb:"]
        for prod, qty in self.items.items():
            ausgabe.append(f"  - {prod.name} x{qty}")
            # Zwischensumme anzeigen.
        ausgabe.append(f"Zwischensumme: {self.berechne_subtotal():.2f}€")
        # Rabatt anzeigen, falls vorhanden.
        rate = self.berechne_rabatt_rate()
        if rate > 0:
            ausgabe.append(f"Rabatt: {int(rate*100)}%")
            # Gesamtbetrag ausgeben.
        ausgabe.append(f"Gesamt: {self.berechne_subtotal() * (1-rate):.2f}€")
        return "\n".join(ausgabe)


def main_interactive():
    # 1) Erstelle Beispielprodukte und ein Lookup-Dict nach Namen (lowercase):
    # Daten anlegen
    p1 = Produkt("T-Shirt", 19.99, 10)
    p2 = Produkt("Jeans", 49.90, 5)
    p3 = Produkt("Sneaker", 79.00, 3)
    alle_produkte = {p.name.lower(): p for p in (p1, p2, p3)}

    # 2) Frage den Nutzer nach seinem Namen und erstelle Kunde und Warenkorb:
    name = input("Hallo lieber Kunde, wie ist ihr Name? ")
    kunde = Kunde(name)
    warenkorb = Warenkorb(kunde)

    # 3) Hauptschleife: wiederholt Anzeige und Abfragen:
    while True:
        # 3a) Immer aktuelle Produktliste mit Lagerstand anzeigen: // # Produkte immer anzeigen //
        print("\nVerfügbare Produkte:")
        for prod in alle_produkte.values():
            print(f"- {prod.name} ({prod.preis:.2f}€) - Lager: {prod.bestand}")

        # 3b) Menü anzeigen und Auswahl einlesen:
        print("\nMenü:")
        print("1) Produkt in Warenkorb legen")
        print("2) Warenkorb bestellen")
        print("3) Bestellhistorie anzeigen")
        print("4) Beenden")
        wahl = input("Deine Wahl: ")

        # 3c) Je nach Eingabe verschiedenen Ablauf:
        if wahl == "1":
            # Produktname eingeben und prüfen, ob es existiert:
            name_prod = input("Produktname: ").strip().lower()
            if name_prod not in alle_produkte:
                print("Unbekanntes Produkt.")
                continue    # zurück zum Menü, ohne Menge abzufragen
            # Menge erfragen und ins Warenkorb-Objekt eintragen:
            menge = int(input("Menge: "))
            try:
                warenkorb.produkt_hinzufuegen(alle_produkte[name_prod], menge)
                print(f"{menge}× {alle_produkte[name_prod].name} hinzugefügt.")
            except ValueError as e:
                # Fängt Fehler ab, z.B. wenn Bestand nicht ausreicht
                print(e)
        elif wahl == "2":
            # Check-out: Bestellung erzeugen und ausgeben
            best = warenkorb.checkout()
            print("Bestellung abgeschlossen:\n", best)
        elif wahl == "3":
            # Alle bisherigen Bestellungen des Kunden anzeigen
            print(f"\nBestellhistorie von {kunde.name}:")
            for b in kunde.bestellungen:
                print(b, "\n")
        elif wahl == "4":
            # Beendet die Schleife und damit das Programm
            print("Auf Wiedersehen!")
            break
        else:
            # Bei ungültiger Eingabe Hinweismeldung
            print("Ungültige Wahl.")

# Dieser Block sorgt dafür, dass main_interactive() nur ausgeführt wird,
# wenn die Datei direkt (nicht als Modul) gestartet wird.
if __name__ == "__main__":
    main_interactive()
