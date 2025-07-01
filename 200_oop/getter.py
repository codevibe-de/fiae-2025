class A:
    __name:str
    def __init__(self, name: str):
        super().__init__()
        self.__name = name
    def get_name(self) -> str:
        return self.__name

class B(A):
    def __init__(self, x:int):
        super().__init__(str(x))
    def get_name(self) -> str:
        return f"Name from B: {self.__name}"


b = B(1)
print(b.get_name())