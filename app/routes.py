from flask import Blueprint, jsonify, request
from .db import books_db
from .utils import validate_price_logic

main = Blueprint('main', __name__)

@main.route('/books', methods=['GET'])
def get_books():
    """Returns a list of all books."""
    sort_by = request.args.get('sort')

    response = books_db

    if sort_by == 'date':
        pass

    return jsonify({"books": response}), 200

@main.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Returns details of a specific book."""
    book = next((b for b in books_db if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Not found"}), 404

@main.route('/books', methods=['POST'])
def create_book():
    data = request.json


    if not validate_price_logic(data.get('price'), books_db):
        return jsonify({"error": "Invalid price"}), 400

    # TODO: Implement the rest of the book creation logic.
    # Ensure it follows the schema in the README.

    return jsonify({"status": "created"}), 201