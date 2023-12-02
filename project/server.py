from flask import Flask, jsonify, request, abort
from catsDAO import catsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#GET
@app.route('/cats')
def getAll():
    results = catsDAO.getAll()
    return jsonify(results)

#GETBYID
@app.route('/cats/<int:id>')
def findById(id):
    foundCat = catsDAO.findByID(id)

    return jsonify(foundCat)

#POST
@app.route('/cats', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    cat = {
        "name": request.json['name'],
        "age": request.json['age'],
        "breed": request.json['breed'],
    }
    values =(cat['name'],cat['age'],cat['breed'])
    newId = catsDAO.create(values)
    cat['id'] = newId
    return jsonify(cat)

#PUT
@app.route('/cats/<int:id>', methods=['PUT'])
def update(id):
    foundCat = catsDAO.findByID(id)
    if not foundCat:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'breed' in reqJson and type(reqJson['breed']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundCat['name'] = reqJson['name']
    if 'age' in reqJson:
        foundCat['age'] = reqJson['age']
    if 'breed' in reqJson:
        foundCat['breed'] = reqJson['breed']
    values = (foundCat['name'],foundCat['age'],foundCat['breed'],foundCat['id'])
    catsDAO.update(values)
    return jsonify(foundCat)

#DELETE
@app.route('/cats/<int:id>' , methods=['DELETE'])
def delete(id):
    catsDAO.delete(id)
    return jsonify({"done":True})



if __name__ == "__main__":
    app.run(debug = True)