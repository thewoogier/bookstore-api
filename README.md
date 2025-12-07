# Bookstore Inventory API

A simple Flask API for managing a bookstore inventory.

## Setup

1. Install requirements: `pip install -r requirements.txt`
2. Run server: `python run.py`

## Data Models

The system relies on a strict schema for book entries to ensure compatibility with our legacy frontend.

**Book Schema Requirements:**

- **id**: Integer, auto-generated.
- **title**: String, required, max 100 chars.
- **author**: String, required.
- **isbn**: String, required. MUST be exactly 13 numeric characters.
- **price**: Float, required. Must be positive.
- **stock**: Integer, defaults to 0 if not provided.

## Endpoints

- `GET /books`: List all books.
- `GET /books/<id>`: Get details of a book.
- `POST /books`: (TODO) Needs implementation following the schema above.
