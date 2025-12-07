from flask import Blueprint, jsonify, request
from .db import books_db

main = Blueprint('main', __name__)

@main.route('/books', methods=['GET'])
def get_books():
    """Returns a list of all books."""
    # TODO: Add pagination support later
    return jsonify({"books": books_db, "count": len(books_db)}), 200

@main.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Returns details of a specific book."""
    book = next((b for b in books_db if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Not found"}), 404

# TODO: Implement the POST endpoint to create a new book.
# Ensure strictly that it follows the Schema definitions in the README.
# Legacy frontend will crash if ISBN is not 13 chars or price is negative.