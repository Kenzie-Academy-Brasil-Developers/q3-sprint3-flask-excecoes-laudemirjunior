from .function import add
from .assistant import create, read
from flask import Flask, request, jsonify
from .exception import EmailError, ValueError


app = Flask(__name__)

@app.get('/user')
def get_user():

    create()

    return jsonify(data= read()), 200

@app.post('/user')
def post_user():

    create()

    request_user = request.get_json()

    database = read()

    try:
        if type(request_user['nome']) != str or type(request_user['email']) != str:
            raise ValueError

        name = request_user["nome"].title()
        email = request_user["email"].lower()
        size = len(database) + 1
        user = {'nome': name, 'email': email, 'id': size}

        add(request_user ,database, user)

    except ValueError:
        return {
    "wrong fields": [
        {
            "nome": str(type(request_user['nome'])).replace("<class '",'').replace("'>",'')
        },
        {
            "email": str(type(request_user['email'])).replace("<class '",'').replace("'>",'')
        }
    ]
  }, 400

    except EmailError:
        return jsonify(error= "Email already exists."), 409
        
    return jsonify(data= [user]), 201
