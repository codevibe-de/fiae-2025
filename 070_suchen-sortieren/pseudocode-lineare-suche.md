# Lineare Suche

## Pseudocode

Mit `for` Loop:
````
liste = [ ... ]
suchwert = 99
ergebnis = -1
FOR i = 0 TO len(liste)-1
    IF liste[i] == suchwert:
        ergebnis = i
        BREAK
    END IF
END FOR
PRINT(ergebnis)
````

A la `while`:

````
liste = [ ... ]
suchwert = 99
ergebnis = -1
i = 0
WHILE i < len(liste) AND ergebnis == -1:
    IF liste[i] == suchwert:
        ergebnis = i
    END IF
    i = i + 1
END WHILE
PRINT(ergebnis)
````

Noch kompakter:

````
liste = [ ... ]
suchwert = 99
i = 0
WHILE i < len(liste) AND liste[i] != suchwert:
    i = i + 1
END WHILE
PRINT(i)
````