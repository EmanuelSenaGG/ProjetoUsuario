from Crud_app import app
import json
from flask import jsonify, request
from Crud_app.models.usuario import Usuario
from Crud_app.business.usuario import sign_in, get_users, sign_up




@app.route('/cadastrar', methods=['POST'])
def create():
 try:
        body = request.get_json()
        usuario = sign_up(body)
        usuarioId = Usuario.from_map(usuario)
        return str(usuarioId.Id), 201
 except Exception as e:
        return e.args, 400
    
@app.route('/login', methods=['POST'])
def login():
    try:
        json_request = request.get_json()
        usuario = Usuario.from_map(json_request)
        usuario_id = sign_in(usuario)
        return usuario_id, 200
    except OSError as e:
        return e.args, 404
    except Exception as e:
        return e.args[0], 400 

    

    
@app.route('/usuarios', methods=['GET'])
def get_all_users():
    try:
        users = get_users()
        return users
    except Exception as e:
        return e.args, 400