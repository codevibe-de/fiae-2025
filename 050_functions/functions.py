def print_greeting():
    print("Hello!")

print_greeting()



def say_hello(name: str, count: int = 1):
    print(f"Hello {name}\n" * count)

say_hello("Boris", 3)
say_hello("Olaf")
say_hello(count=2, name="Jorge")



def prefix_names(prefix:str="", *names:str):
    for name in names:
        print(prefix + name)

prefix_names()
prefix_names(">")
prefix_names(">", "Alice", "Bob", "Charlie")
