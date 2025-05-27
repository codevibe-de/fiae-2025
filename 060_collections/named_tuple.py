from collections import namedtuple

Vehicle = namedtuple("Fahrzeug", ["speed", "armor"])

tank = Vehicle(speed=12, armor=7)
apc = Vehicle(speed=28, armor=2)
print(tank)
print(apc.speed)