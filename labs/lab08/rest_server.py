from flask import Flask, url_for, request, redirect, abort, jsonify
app = Flask(__name__, static_url_path='', static_folder='staticpages')
books=[
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
    {"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
    {"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500},
]
nextId=4

#get all
#curl http://127.0.0.1/books
@app.route('/books')
def getAll():
    return jsonify(books)

# find By id
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}) , 204
    return jsonify(foundBooks[0])

# create
@app.route('/books', methods=['POST'])
def create():
    global nextId
    book = {
        "id": nextId,
        "Title": "Test",
        "Author": "Test",
        "Price": 999
    }
    books.append(book)
    nextId += 1
    return jsonify(book)

#update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    return "served by update with it " + str(id)

#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return "served by delete with it " + str(id)
def index():
    return "hello"
if __name__ == "__main__":
    app.run(debug=True)