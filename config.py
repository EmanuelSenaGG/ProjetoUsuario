import pyrebase

FireBaseConfig = { 
        "apiKey": "AIzaSyAjyx6FeggWZfLo29sovbdbX-nGwSHluos",
        "authDomain": "crudusuario-74619.firebaseapp.com",
        "databaseURL": "https://crudusuario-74619-default-rtdb.firebaseio.com",
        "projectId": "crudusuario-74619",
        "storageBucket": "crudusuario-74619.appspot.com",
        "messagingSenderId": "687078185511",
        "appId": "1:687078185511:web:cc2deabc2bbb8668188c02"
        }

firebase = pyrebase.initialize_app(FireBaseConfig)
auth = firebase.auth()