

values = [5, 12, -2, 0]
l = len(values)
first = values[0]

if values:
    last = values[-1]  # zählt vom ENDE der Liste
    print(last)
else:
    print("No values")

items = []
items.append("blah")
items.append("abc")
items.insert(0, "first")
items.sort()
del items[2]
items.remove("blah")
exists: bool = "first" in items
n = items.index("abc")
items.clear()
print(exists, n)

lst = [1]
lst.insert(0, 0)
lst.append(99)
print(type(lst))

empty = list()

# ----------------------

names = ["Bob", "Joe"]
for n in names:
    print(n)


# Typed lists:

from typing import List

my_numbers: List[int] = [123, 55, -1, 42]
not_good: List[str] = [True, 123, 33.0]


# Slicing

vowels = ["a", "e", "i", "o", "u"]
first_two = vowels[:2] # ['a', 'e']
last_two = vowels[-2:] # ['o', 'u']
every_second = vowels[::2] # ['a', 'i', 'u']
