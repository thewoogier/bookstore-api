# Bookstore Inventory API v2

A Flask API for managing a bookstore inventory.

## Setup

1. Install: `pip install -r requirements.txt`
2. Run: `python run.py`

## Architecture Rules

1. **Concurrency**: All database operations must be thread-safe.
2. **Legacy Support**: We use a `dict` based storage in memory. Do not switch to SQL.

## Data Models (Strict Schema)

**Book Entry:**

- **id**: Integer.
- **title**: String.
- **author**: String.
- **isbn**: String. MUST be exactly 13 numeric characters.
- **price**: Float. MUST be positive.
- **status**: String. Allowed values: "active", "archived". (Defaults to "active").

## Endpoints

- `GET /books`: List all books.
- `GET /books/<id>`: Get details of a specific book.
- `POST /books`: (TODO) Needs implementation. Must follow the Strict Schema defined above.

## Authentication

**Note:** All write operations (POST/PUT/DELETE) require the `X-API-Key` header.
_See `app/auth_middleware.py` for implementation details._

## Known Issues

- The pricing validator in `utils.py` is currently O(N) relative to inventory size. We need this to be O(1) without changing the data structure.
