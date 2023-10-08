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
        
        response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': usuario
    }
        
      
       
        return response, 200
 except Exception as e:
        return e.args, 400
    
@app.route('/login', methods=['POST'])
def login():
    try:
        body = request.get_json()
        #usuario = Usuario.from_map(json_request)
        usuario = sign_in(body)
        response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': usuario
    }
        
     
       
        return response, 200
    except OSError as e:
        return e.args, 404
  

    
@app.route('/usuarios', methods=['GET'])
def get_all_users():
    try:
        users = get_users() 
        return users
    except Exception as e:
        return e.args, 400
    
@app.route('/index', methods=['GET'])
def home():
    try:
        return 'olaaaaaaaaa'
    except Exception as e:
        return e.args, 400