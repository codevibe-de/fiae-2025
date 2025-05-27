import sys

# range(start, stop, step)
for n in range(5, 0, -1):
    print(n)
print("Lift off!")

print("-" * 40)


for i in range(3):
    for j in range(2):
        print(i, j)

print("-" * 40)


for b1 in [False, True]:
    for b2 in [False, True]:
        print(b1, b2, b1 and b2)

print("-" * 40)


x = 64
while x % 2 == 0:
    print(x)
    x = x // 2

print("-" * 40)


for arg in sys.argv:
    print(arg)

print("-" * 40)

words = ["hello", "world"]
for i, word in enumerate(words):
    print(i, word)

print("-" * 40)

my_dict = {"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for key, value in my_dict.items():
    print(key, value)
