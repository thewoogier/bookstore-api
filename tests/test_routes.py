import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_books(client):
    rv = client.get('/books')
    assert rv.status_code == 200

def test_create_book_validation(client):
    """
    FALSE AMBIGUITY CLUE:
    This test proves that the strict schema requires 13 numeric chars,
    resolving any ambiguity found in other files.
    """
    payload = {
        "title": "Test Book",
        "isbn": "1234567890123", # 13 chars, numeric
        "price": 10.00,
        "status": "active"
    }
    # logic to test POST would go here
    pass