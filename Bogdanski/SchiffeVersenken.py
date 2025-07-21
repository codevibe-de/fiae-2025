'''SchiffeVersenken'''

class Spielfeld():

    def __init__(self):
        self.spielfeld=self.creat_spielfeld

    def creat_spielfeld(self):
        spielfeld=[[0 for _ in range(10)] for _ in range(10)]

    def print_spielfeld(self):
        for row in self.spielfeld:
            print(row)

class spieler():
    name:str
    schiff_liste:list
    spielerspielfeld:Spielfeld
    mirrorspielfeld:Spielfeld
    def __init__(self, name,schiff_liste):
        self.name=name
        self.schiff_liste=schiff_liste
        self.spielerspielfeld.creat_spielfeld()

class schiffe():
    größe:list
    name:str
    menge:int

    def __init__(self,name,größe,menge):
        self.name=name
        self.größe=[[1 for _ in range(größe)] for _ in range(1)]
        self.menge=menge
# class spielregeln():




kreuzer=schiffe("kreuzer",4,2)
spiel_schiffe=[kreuzer]
spieler1=spieler("Spieler1",spiel_schiffe)
spieler1.spielerspielfeld.print_spielfeld()