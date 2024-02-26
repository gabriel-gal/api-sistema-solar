from flask import Flask, make_response, jsonify
from bd import Planetas

app = Flask(__name__)

@app.route('/planetas', methods=['GET'])
def get_planetas():
    return make_response( 
        jsonify(Planetas) 
    ) 

@app.route('/planetas/{}', methods=['GET'])
def get_planeta_id():
    id = request.args.get('id')
    response = get_book(id)
    return response

if __name__ == "__main__":
    app.run(debug=True)