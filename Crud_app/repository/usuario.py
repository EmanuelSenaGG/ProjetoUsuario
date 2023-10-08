import json
from Crud_app.models.Db import uri_create_user,uri_get_users
import requests
from Crud_app.models.usuario import Usuario
from config import auth
from firebase_admin import auth as admin_auth

def create_firebase(body):
    try:
        usuario = Usuario.from_map(body)
        auth.create_user_with_email_and_password(email = usuario.email, password = usuario.senha)
        request = requests.post(uri_create_user, body)
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
        auth.sign_in_with_email_and_password(email = usuario.email, password=usuario.senha)
        return True
    except:
        raise Exception("Usuario ou senha incorretos!")


