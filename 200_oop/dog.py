class Dog:
    count = 0

    @classmethod
    def new_dog(cls, name):
        cls.count += 1
        return cls(name)

    def __init__(self, name):
        self.name = name


Dog.new_dog("Fido")