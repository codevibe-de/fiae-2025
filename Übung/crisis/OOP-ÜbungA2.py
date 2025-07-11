# Übung 2: Fahrzeug-Hierarchie
# Starter Code für Python
# Erstellen Sie eine Vererbungshierarchie für Fahrzeuge:
# °Basisklasse Fahrzeug mit gemeinsamen Attributen (Marke, Modell, Baujahr)
# °Unterklassen: Auto, Motorrad, LKW
# °Jede Unterklasse hat spezifische Attribute (z.B.Anzahl Türen für Auto, Ladekapazität für LKW)

# Anforderung:
# °Implementieren Sie eine abstrakte Methode fahren() in der Basisklasse
# °Überschreiben Sie die Methode in jeder Unterklasse mit spezifischem Verhalten
# °Implementieren Sie Polymorphismus durch eine gemeinsame Methode fahrzeugInfo()

#Abstract Base Class
from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    def __init__(self, marke, modell, baujahr):
        # TODO: Attribute initialisieren
        pass

    @abstractmethod
    def fahren(self):
        # TODO: Abstrakte Methode - muss in Unterklassen implementiert werden
        pass

    def fahrzeug_info(self):
        # TODO: Gemeinsame Methode für alle Fahrzeuge
        # Soll grundlegende Fahrzeuginfos zurückgeben
        pass

    # TODO: Getter-Methoden implementieren

    def __str__(self):
        # TODO: String-Darstellung des Fahrzeugs
        return ""


class Auto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_tueren):
        # TODO: Parent-Konstruktor aufrufen
        # TODO: Spezifische Attribute initialisieren
        pass

    def fahren(self):
        # TODO: Spezifisches Fahrverhalten für Autos
        pass

    # TODO: Spezifische Methoden für Autos hinzufügen


class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, hubraum):
        # TODO: Parent-Konstruktor aufrufen
        # TODO: Spezifische Attribute initialisieren
        pass

    def fahren(self):
        # TODO: Spezifisches Fahrverhalten für Motorräder
        pass

    # TODO: Spezifische Methoden für Motorräder hinzufügen


class LKW(Fahrzeug):
    def __init__(self, marke, modell, baujahr, ladekapazitaet):
        # TODO: Parent-Konstruktor aufrufen
        # TODO: Spezifische Attribute initialisieren
        pass

    def fahren(self):
        # TODO: Spezifisches Fahrverhalten für LKWs
        pass

        def beladen(self, gewicht):
            # TODO: Methode zum Beladen des LKWs
            # TODO: Prüfen ob Ladekapazität nicht überschritten wird
            pass

    class Fuhrpark:
        def __init__(self):
            # TODO: Liste für Fahrzeuge initialisieren
            pass

        def fahrzeug_hinzufuegen(self, fahrzeug):
            # TODO: Fahrzeug zum Fuhrpark hinzufügen
            pass

        def alle_fahrzeuge_fahren_lassen(self):
            # TODO: Polymorphismus demonstrieren
            # TODO: Für jedes Fahrzeug die fahren()-Methode aufrufen
            pass

        def fuhrpark_info(self):
            # TODO: Informationen über alle Fahrzeuge anzeigen
            pass

    # Test-Code
    if __name__ == "__main__":
        # TODO: Erstellen Sie verschiedene Fahrzeuge
        # TODO: Testen Sie Vererbung und Polymorphismus

        fuhrpark = Fuhrpark()

        # Beispiel-Fahrzeuge erstellen und hinzufügen
        # auto = Auto("BMW", "X5", 2023, 4)
        # motorrad = Motorrad("Harley", "Street", 2022, 750)
        # lkw = LKW("Mercedes", "Actros", 2021, 25000)

        # TODO: Fahrzeuge zum Fuhrpark hinzufügen
        # TODO: Verschiedene Methoden testen