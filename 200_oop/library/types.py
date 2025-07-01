from abc import ABC, abstractmethod

# Interface
class Media(ABC):
    @abstractmethod
    def get_id_number(self) -> str:
        pass

# Abstract base class
class PrintMedia(Media):
    def __init__(self, title: str, id_number: str):
        self.title = title
        self._id_number = id_number

    def get_id_number(self) -> str:
        return self._id_number

# Subclasses
class Book(PrintMedia):
    def __init__(self, title: str, author: str, id_number: str):
        super().__init__(title, id_number)
        self.author = author

class Magazine(PrintMedia):
    def __init__(self, title: str, issue: int, id_number: str):
        super().__init__(title, id_number)
        self.issue = issue