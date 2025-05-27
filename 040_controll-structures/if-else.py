a = int(input("Eine Zahl bitte: "))

if a < 10:
    print("single digit")
elif a < 100:
    print("double digit")
elif a < 1000:
    print("triple digit")
else:
    print("large")


if 1 == 1:
    print("truthy")
if "blah":
    print("truthy")
if 72072:
    print("truthy")