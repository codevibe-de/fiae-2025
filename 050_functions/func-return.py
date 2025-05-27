# Simple function -- no parameters, single value return
def get_name() -> str:
    return "Yoda"

my_name = get_name()


# Function returns two values
def get_name_and_age() -> (str,int):
    return get_name(), 123

n,a = get_name_and_age()
print(f"{n} is {a} years old")

