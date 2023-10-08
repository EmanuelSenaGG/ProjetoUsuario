from Crud_app.repository.usuario import create_firebase, list_users, login_firebase

def sign_up(body):
     try:
       return create_firebase(body)
     except:
       raise

def sign_in(body):
  try:
    return login_firebase(body)
  except:
     raise
   
def get_users():
  try:
    return list_users()
  except:
    raise