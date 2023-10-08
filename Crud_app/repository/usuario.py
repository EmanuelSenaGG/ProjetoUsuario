import json
from Crud_app.models.Db import uri_create_user,uri_get_users
import requests
from Crud_app.models.usuario import Usuario
from config import auth
from firebase_admin import auth as admin_auth

def create_firebase(data):
    try:
        usuario = Usuario.from_map(data)
        #token = auth.create_user_with_email_and_password(email = usuario.email, password = usuario.senha)
        headers = {"content-type": "application/json; charset=UTF-8"}
        body = json.dumps(data)
        request = requests.post(uri_create_user, headers=headers, data=body) 
        return  request.text
    except Exception as e:
        raise Exception("Já existe uma conta com esse email!")
    
def list_users():
    try:
        request = requests.get(uri_get_users)
        return request.text
    except:
        raise Exception("Não foi possível localizar os usuários!")



def login_firebase(body):
    try:
        usuario = Usuario.from_map(body)
        token = auth.sign_in_with_email_and_password(email = usuario.email, password=usuario.senha)
        return token
    except:
        raise Exception("Usuario ou senha incorretos!")


