from dataclasses import dataclass

@dataclass
class Book:
    """
    Strict definition of a Book.

    CONFLICTING REQUIREMENT TARGET:
    - This class defines 'is_published' (bool), but the database and README use 'status' (str).
    - This class allows ISBN to include dashes, but README says "numeric characters only".
    """
    id: int
    title: str
    isbn: str
    price: float
    is_published: bool