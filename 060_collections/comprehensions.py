import math

numbers = [12, 23, 42, 4, 3, 2, 1]
squares = [n * n for n in numbers]
# ODER: squares = list(n * n for n in numbers)

# Comprehension mit zusätzlicher Bedingung - und auf mehrere Zeilen verteilt für bessere Lesbarkeit
roots_of_even_numbers = [
    math.sqrt(x)
    for x in numbers
    if x % 2 == 0
]
