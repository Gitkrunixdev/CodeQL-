from flask import request, render_template
from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = request.args.get('read')

    books = []

    if name:
        query = "SELECT name, author, read FROM books WHERE name LIKE %s"
        cursor.execute(query, (f"%{name}%",))
        books = [Book(*row) for row in cursor]

    elif author:
        query = "SELECT name, author, read FROM books WHERE author LIKE %s"
        cursor.execute(query, (f"%{author}%",))
        books = [Book(*row) for row in cursor]

    elif read is not None:
        query = "SELECT name, author, read FROM books WHERE read = %s"
        cursor.execute(query, (read,))
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)
