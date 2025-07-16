class Something:


    def __init__(self):
        self.counter = None

    def calc(a: int, b:int):
        return a + b

    def increment(self):
        counter = self.counter + 1
        return counter

    def __str__(self):
        return super().__str__()


r = Something.calc(1,2)
