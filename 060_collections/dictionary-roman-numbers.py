roman_numbers = {"I": 1}
print(roman_numbers['I'])

roman_numbers['V'] = 5
roman_numbers['X'] = 10

for k, v in roman_numbers.items():
    print(f"{k} -> {v}")