from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    def __init__(self, marke, modell, baujahr):
        self._marke = marke
        self._modell = modell
        self._baujahr = baujahr

    @abstractmethod
    def fahren(self):
        """Abstrakte Methode, die in Unterklassen implementiert wird."""
        pass

    def fahrzeug_info(self):
        """Gibt grundlegende Fahrzeuginformationen als String zurück."""
        return f"{self._baujahr}er {self._marke} {self._modell}"

    def get_marke(self):
        return self._marke

    def get_modell(self):
        return self._modell

    def get_baujahr(self):
        return self._baujahr

    def __str__(self):
        return self.fahrzeug_info()


class Auto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_tueren):
        super().__init__(marke, modell, baujahr)
        self.anzahl_tueren = anzahl_tueren

    def fahren(self):
        print(f"Das Auto {self._marke} {self._modell} fährt komfortabel mit {self.anzahl_tueren} Türen.")

#Spezifische Attribute initialisieren
    def hupen(self):
        print("Hupe hupt!")


class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, hubraum):
        super().__init__(marke, modell, baujahr)
        self.hubraum = hubraum

    def fahren(self):
        print(f"Das Motorrad {self._marke} {self._modell} mit {self.hubraum}ccm fährt agil über Landstraßen.")

#Spezifische Attribute initialisieren
    def wheelie(self):
        print("Das Motorrad macht einen Wheelie!")


class LKW(Fahrzeug):
    def __init__(self, marke, modell, baujahr, ladekapazitaet):
        super().__init__(marke, modell, baujahr)
        self.ladekapazitaet = ladekapazitaet
        self.current_ladung = 0

    def fahren(self):
        print(f"Der LKW {self._marke} {self._modell} transportiert {self.current_ladung}kg Ladung.")

    def beladen(self, gewicht):
        if self.current_ladung + gewicht > self.ladekapazitaet:
            print(f"Fehler: Ladekapazität von {self.ladekapazitaet}kg überschritten!")
        else:
            self.current_ladung += gewicht
            print(f"{gewicht}kg beladen, aktueller Ladestand: {self.current_ladung}kg.")


class Fuhrpark:
    def __init__(self):
        self.fahrzeuge = []

    def fahrzeug_hinzufuegen(self, fahrzeug):
        if isinstance(fahrzeug, Fahrzeug):
            self.fahrzeuge.append(fahrzeug)
        else:
            print("Nur Objekte vom Typ Fahrzeug können hinzugefügt werden.")

    def alle_fahrzeuge_fahren_lassen(self):
        for fz in self.fahrzeuge:
            fz.fahren()

    def fuhrpark_info(self):
        for fz in self.fahrzeuge:
            print(fz)


if __name__ == "__main__":
    # Fuhrpark erstellen
    fuhrpark = Fuhrpark()

    # Beispiel-Fahrzeuge erstellen
    auto = Auto("BMW", "X5", 2023, 4)
    motorrad = Motorrad("Harley-Davidson", "Street 750", 2022, 750)
    lkw = LKW("Mercedes", "Actros", 2021, 25000)

    # Fahrzeuge zum Fuhrpark hinzufügen
    fuhrpark.fahrzeug_hinzufuegen(auto)
    fuhrpark.fahrzeug_hinzufuegen(motorrad)
    fuhrpark.fahrzeug_hinzufuegen(lkw)

    # Informationen über den Fuhrpark ausgeben
    print("--- Fuhrpark-Info ---")
    fuhrpark.fuhrpark_info()
    print()

    # Alle Fahrzeuge fahren lassen
    print("--- Fahrzeuge fahren ---")
    fuhrpark.alle_fahrzeuge_fahren_lassen()
    print()

    # LKW beladen und erneut fahren lassen
    print("--- LKW Beladungstest ---")
    lkw.beladen(10000)
    lkw.beladen(16000)
    lkw.fahren()
