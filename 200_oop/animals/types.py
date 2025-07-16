class Animal:
    name: str
    def __init__(self, name:str):
        print("Constructing an animal...");
        self.name = name
    def say_hello(self, greetee: str):
        print("Hi "+ greetee + ", my name is " + self.name)

class Mammal(Animal):
    averageNumberOfPups: float

class Whale(Mammal):
    maxDivingDepth: int

class Fish(Animal):
    pass

class Shark(Fish):
    def say_hello(self, greetee: str):
        print("Here is " + self.name)
    # method overloading not natively supported
    def bite(self, animal):
        if isinstance(animal, Animal):
            self.bite(animal.name)
        elif isinstance(animal, str):
            print("Biting " + animal + " because I am hungry!!")
        else:
            raise TypeError("neither Animal nor str")


hugo = Whale("Hugo")
hugo.say_hello("Max")

bruce = Shark("Bruceee")
bruce.say_hello("Sonstwen")
bruce.bite(hugo)
bruce.bite(42)
