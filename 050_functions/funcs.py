# Most simple function -- no input, no output
def foo():
    print("Foo!!")


# Function with two parameters, last one having a default value
def baz(s: str, count: int = 1):
    print(s * count)


baz("hey", count=10)
