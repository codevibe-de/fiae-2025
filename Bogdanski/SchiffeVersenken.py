'''SchiffeVersenken'''

from numpy.core.defchararray import capitalize



class Spielfeld():
    spielfeld: list

    def __init__(self, wert=0):
        self.spielfeld = [[wert for _ in range(10)] for _ in range(10)]

    # def creat_spielfeld(self):
    #     self.spielfeld=[[0 for _ in range(10)] for _ in range(10)]
    def spielfeldsetter(self, x, y, wert):
        spiel_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        z = spiel_map[x]
        self.spielfeld[y][z] = wert

    def treffer_prüfung(self, x, y):
        spiel_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        z = spiel_map[x]
        if self.spielfeld[y][z] == 1:
            self.spielfeld[y][z] = 0
            return True
        else:
            return False

    def print_spielfeld_platzieren(self):  # zum printen von dem Feld mit den angezeigten 0en und 1en
        i = 0
        print("   A  B  C  D  E  F  G  H  I  J")
        for row in self.spielfeld:
            print(f"{i} {str(row)}")
            i += 1

    def print_spielfeld_spiel(self):  # für den print von dem verschleierten spielfeld
        i = 0
        print("    A    B    C    D    E    F    G    H    I    J")
        for row in self.spielfeld:
            print(f"{i} {str(row)}")
            i += 1


class schiffe():
    größe: list
    name: str
    menge: int

    def __init__(self, name, größe, menge):
        self.name = name
        self.größe = [1 for _ in range(größe)]
        self.menge = menge

    def länge(self):
        return len(self.größe)

    def ist_schiff_zerstört(self):
        tem=0
        for x in self.größe:
            if x != 0:
                tem+=1
        if tem!=0:
            return False
        else:
            return True


class spieler():
    name: str
    spielerspielfeld: Spielfeld
    kreuzer: schiffe
    fischer: schiffe
    schiff_liste: list
    spiegelfeld: Spielfeld
    gesetze_schiffe:list

    def __init__(self, name, ):
        self.name = name
        self.spielerspielfeld = Spielfeld()
        self.spiegelfeld = Spielfeld("x")
        self.kreuzer = schiffe("kreuzer", 4, 1)
        self.fischer = schiffe("Fischerboot", 2, 1)
        self.schiff_liste = list()
        self.schiff_liste.append(self.kreuzer)
        self.schiff_liste.append(self.fischer)
        self.gesetze_schiffe = list()

    def schiff_wurde_gesetzt(self, schiff: schiffe):
        schiff.menge -= 1  # menge des schiffes um 1 reduzieren
        if schiff.menge == 0:  # prüft ob noch schiffe von der sorte vorhanden sind
            self.schiff_liste.remove(schiff)  # wenn keine vorhanden dann wird gelöscht aus der liste
            self.gesetze_schiffe.append(schiff)

    def schiff_auf_feld_prüfen(self,x1,y1,x2,y2):
        spiel_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        reverse_spiel_map = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
        z1 = spiel_map[x1]
        z2 = spiel_map[x2]
        if len(self.gesetze_schiffe)>=1:
            for schiff in self.gesetze_schiffe:
                for x in schiff.größe:
                    if z1 == z2:
                        if y2 > y1:
                            y_start = y1
                            y_ende = y2
                        else:
                            y_start = y2
                            y_ende = y1
                        for i in range(y_start,y_ende+1):
                            if x == (x1,i):
                                return False
                    if y1 == y2:
                        if z2 > z1:
                            x_start = z1
                            x_ende = z2
                        else:
                            x_start = z2
                            x_ende = z1
                        for i in range(x_start, x_ende + 1):
                            if x == (reverse_spiel_map[i],y1):
                                return False
        return True

    def schiff_auf_feld_festsetzen(self,schiff:schiffe,x1,y1,x2,y2):
        spiel_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        reverse_spiel_map = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
        z1 = spiel_map[x1]
        z2 = spiel_map[x2]
        n=0
        if z1==z2:
            if y2>y1:
                y_start=y1
                y_ende=y2
            else:
                y_start = y2
                y_ende = y1
            for i in range(y_start,y_ende+1):
                schiff.größe[n]=(x1,i)
                n+=1
        if y1==y2:
            if z2>z1:
                x_start=z1
                x_ende=z2
            else:
                x_start = z2
                x_ende = z1
            for i in range(x_start,x_ende+1):
                schiff.größe[n]=(reverse_spiel_map[i],y1)
                n+=1

    def schiff_treffer(self,x,y):
        if len(self.gesetze_schiffe) >= 1:
            for schiff in self.gesetze_schiffe:
                for i in range(len(schiff.größe)):
                    if schiff.größe[i]==(x,y):
                        schiff.größe[i]=0
                    if schiff.ist_schiff_zerstört():
                        self.gesetze_schiffe.remove(schiff)
                        print(f"{schiff.name} wurde zerstört!")
                        return
        return False

    def game_state(self):
        for x in self.spielerspielfeld.spielfeld:
            for i in x:
                if 1 in x:
                    return True
        return False


class spielregeln():
    a = 0

    def platzieren(self, Spieler: spieler, schiff: schiffe, x1, y1, x2, y2):
        spiel_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        reverse_spiel_map = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
        z1 = spiel_map[x1]
        z2 = spiel_map[x2]

        if Spieler.schiff_auf_feld_prüfen(x1, y1, x2, y2): #prüfen ob dort bereits ein schiff gesetzt wurde
            if z1 == z2:  # prüft ob gesetzer x value gleich ist
                if y1 > y2:
                    if schiff.länge() == (y1 + 1 - y2):
                        for y in range(y2, y1 + 1):
                            Spieler.spielerspielfeld.spielfeldsetter(x1, y, 1)
                        Spieler.schiff_wurde_gesetzt(schiff)  # reduziert die menge der Schiffe um 1 und prüft ob menge 0 ist, deleted dann aus der schiff_liste des Spielers
                        Spieler.schiff_auf_feld_festsetzen(schiff, x1, y1, x2, y2) #das schiff mit den gesetzten koordinaten füllen
                    else:
                        print("Schiff kann hier nicht platziert werden")
                elif y2 > y1:
                    if schiff.länge() == (y2 + 1 - y1):
                        for y in range(y1, y2 + 1):
                            Spieler.spielerspielfeld.spielfeldsetter(x1, y, 1)
                        Spieler.schiff_wurde_gesetzt(schiff)  # reduziert die menge der Schiffe um 1 und prüft ob menge 0 ist, deleted dann aus der schiff_liste des Spielers
                        Spieler.schiff_auf_feld_festsetzen(schiff, x1, y1, x2, y2) #das schiff mit den gesetzten koordinaten füllen

                    else:
                        print("Schiff kann hier nicht platziert werden")
            elif y1 == y2:  # prüft ob gesetzer y value gleich ist
                if z1 > z2:
                    if schiff.länge() == (z1 + 1 - z2):
                        for x in range(z2, z1 + 1):
                            x_val = reverse_spiel_map[x]
                            Spieler.spielerspielfeld.spielfeldsetter(x_val, y1, 1)
                        Spieler.schiff_wurde_gesetzt(schiff)  # reduziert die menge der Schiffe um 1 und prüft ob menge 0 ist, deleted dann aus der schiff_liste des Spielers
                        Spieler.schiff_auf_feld_festsetzen(schiff, x1, y1, x2, y2) #das schiff mit den gesetzten koordinaten füllen

                    else:
                        print("Schiff kann hier nicht platziert werden")
                elif z2 > z1:
                    if schiff.länge() == (z2 + 1 - z1):
                        for x in range(z1, z2 + 1):
                            x_val = reverse_spiel_map[x]
                            Spieler.spielerspielfeld.spielfeldsetter(x_val, y1, 1)
                        Spieler.schiff_wurde_gesetzt(schiff)  # reduziert die menge der Schiffe um 1 und prüft ob menge 0 ist, deleted dann aus der schiff_liste des Spielers
                        Spieler.schiff_auf_feld_festsetzen(schiff, x1, y1, x2, y2) #das schiff mit den gesetzten koordinaten füllen

                    else:
                        print("Schiff kann hier nicht platziert werden")
        else:
            print("Schiffe dürfen sich nicht überschneiden")

    def spieler_wechsel(self):
        if self.a == 0:
            self.a = 1
            return spieler1.spielerspielfeld
        if self.a == 1:
            self.a = 0
            return spieler2.spielerspielfeld

    def aktueller_spieler(self):
        if self.a == 0:
            return spieler1
        else:
            return spieler2

    def aktueller_schütze(self):
        if self.a == 0:
            return spieler2
        else:
            return spieler1

    def schießen(self, x, y):
        if self.aktueller_spieler().spielerspielfeld.treffer_prüfung(x, y) == True:
            self.aktueller_spieler().spiegelfeld.spielfeldsetter(x, y, "1")
            print("Treffer!")
            self.aktueller_spieler().schiff_treffer(x,y)
            return
        if self.aktueller_spieler().spielerspielfeld.treffer_prüfung(x, y) == False:
            self.aktueller_spieler().spiegelfeld.spielfeldsetter(x, y, "0")
            print("Nicht getroffen :(")
            return

    def spielstart_platzieren(self):
        while (len(self.aktueller_spieler().schiff_liste) > 0):
            self.aktueller_spieler().spielerspielfeld.print_spielfeld_platzieren()
            for i in self.aktueller_spieler().schiff_liste:
                print(f"Noch {len(self.aktueller_spieler().schiff_liste)} Schiffe zu setzen")
                print(f"{self.aktueller_spieler().name} muss seinen {i.name} setzen mit der größe {i.länge()}x1")
                eingabe = input("gib das erste Feld ein von wo aus bis wo dein Schiff gesetzt werden soll: ")
                von_wo = eingabe.split()
                eingabe = input("gib das zweite Feld bis wohin dein Schiff gesetzt werden soll: ")
                bis_wo = eingabe.split()
                Spiel.platzieren(self.aktueller_spieler(), i, str(capitalize(von_wo[0])), int(von_wo[1]),
                                 str(capitalize(bis_wo[0])),
                                 int(bis_wo[1]))
        self.aktueller_spieler().spielerspielfeld.print_spielfeld_platzieren()

def spielen():
    while (spieler1.game_state() == True and spieler2.game_state() == True):
        Spiel.spieler_wechsel()
        print(f"Das Spielfeld von {Spiel.aktueller_spieler().name} wird gezeigt")
        Spiel.aktueller_spieler().spiegelfeld.print_spielfeld_spiel()
        eingabe = input(
            f"{Spiel.aktueller_schütze().name} darf schießen. Wo soll hingeschossen werden? schreibweise (A 0):  ")
        von_wo = eingabe.split()
        Spiel.schießen(str(capitalize(von_wo[0])), int(von_wo[1]))

def main():
    global Spiel, spieler1, spieler2
    Spiel = spielregeln()
    spieler1 = spieler("Spieler1")
    spieler2 = spieler("Spieler2")
    aktuelles_spielfeld = Spielfeld()
    # Spieler1 fängt an mit dem platzieren seiner Schiffe
    print(f"{Spiel.aktueller_spieler().name} fängt an seine Schiffe zu setzen")
    Spiel.spielstart_platzieren()
    print(Spiel.aktueller_spieler().kreuzer.größe)
    print(Spiel.aktueller_spieler().fischer.größe)
    Spiel.spieler_wechsel()  # auf Spieler 2 wechseln
    # Spieler 2 platziert seine Schiffe
    print(f"{Spiel.aktueller_spieler().name} fängt an seine Schiffe zu setzen")
    Spiel.spielstart_platzieren()
    # setzen der Schiffe Beendet
    print(" Alle Schiffe wurden gesetzt, das Spiel beginnt!")
    Spiel.spieler_wechsel()  # damit vom stand Spieler 1 aus gegangen wird und der Spieler 1 dann mit dem ersten schuss beginnen kann
    # das spiel wird gestartet durch schleife
    spielen()
    Spiel.spieler_wechsel()  # Spielerwechsel damit der richtige gewinner angezeigt wird
    print(f"{Spiel.aktueller_spieler().name} hat das Spiel gewonnen!")


# Main Spiel
main()
