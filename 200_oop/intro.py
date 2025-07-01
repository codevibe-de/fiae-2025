class A:
    DEFAULT_NAME = "Standardname"
    name: str
    price: int

    def __init__(self):
        print("Constructing an instance of A")
        self.name = A.DEFAULT_NAME
        self.price = 0

class B:
    age: int


print(A.DEFAULT_NAME)

meineInstanzVonA = A()  # Constructor Call
print(meineInstanzVonA.name)

foo = B()