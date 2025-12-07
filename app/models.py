from dataclasses import dataclass

@dataclass
class Book:
    """
    Strict definition of a Book.
    """
    id: int
    title: str
    isbn: str
    price: float
    is_published: bool