class A:
    def __str__(self):
        return "I am an instance of class A"

class B(A):
    pass

a = A()
print(a)
print(type(a))