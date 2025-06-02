'''Aufgabe Advent of Code Day 5 Alchemical Reduction'''
def eingabe_in_liste(eingabe):
    return list(eingabe)

def reaktion(polly):
    i=0
    while i<=len(polly)-2:
        if i<0:
            i=0
        if len(polly)>1:
            if polly[i]!=polly[i+1]:
                if polly[i].capitalize()==polly[(i+1)] or polly[i].lower() == polly[(i + 1)] :
                    del polly[i]
                    del polly[i]
                    i-=1
                    continue
        i+=1
    return polly

def ausgabe(wert):
    return ''.join(wert)

# polymer = input("Gebe den ganzen Polymer ein: ")
# resultat = eingabe_in_liste(polymer)
# ergebnis = reaktion(resultat)
# print(ausgabe(ergebnis))

print(ausgabe(reaktion(eingabe_in_liste(input("Gebe den ganzen Polymer ein: ")))))
