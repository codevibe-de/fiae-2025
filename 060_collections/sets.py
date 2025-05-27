colors = {"red", "green", "blue", "red"}
print(len(colors))

empty_set = set()  # NICHT mit {}

colors.add("yellow")
colors.remove("red")
print("green" in colors)
colors.clear()

pastell_colors = {"light pink", "soft green"}

all_colors = colors.union(pastell_colors)
all_colors = colors | pastell_colors

vowels = {'a', 'e', 'i', 'o', 'u'}
letters = {'H', 'e', 'l', 'l', 'o'}
print("Enthaltene Vokale: " + str(vowels & letters))
print("Enthaltene Konsonanten: " + str(letters - vowels))
