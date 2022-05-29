#authentication.py by Mitchell Zarb
import pyrebase
import json

class firebase_authentication():

  def __init__(self):
    self.firebaseConfig = {
      "apiKey": "AIzaSyAfNGIj7JGdK3NZ22i496pkAvQrmvffVyA",
      "authDomain": "ia2-digitalsoltuions.firebaseapp.com",
      "databaseURL": "https://ia2-digitalsoltuions-default-rtdb.firebaseio.com/",
      "projectId": "ia2-digitalsoltuions",
      "storageBucket": "ia2-digitalsoltuions.appspot.com",
      "messagingSenderId": "1059336754959",
      "appId": "1:1059336754959:web:b9aa02ea8761cea2a0907a",
      "measurementId": "G-MBS44P89K1"
    };

    self.firebase=pyrebase.initialize_app(self.firebaseConfig)
    self.auth=self.firebase.auth()


  #Login Function
  def firebase_Login(self, email_address, password):
    print("Logging In...")
    try:
      firebase_Login=self.auth.sign_in_with_email_and_password(email_address, password)
      # Debug
      # print("Successfully Logged In! ")
      uuid_ident=self.auth.get_account_info(firebase_Login['idToken'])
      self.token=firebase_Login['idToken']
      self.uuid=uuid_ident["users"][0]["localId"]
      print(self.uuid, self.token)
    except:
      # Debug
      print("Incorect!Email or Password!")
      return
    

  #SignUp Function
  def firebase_Signup(self, email_address, password):
    print("Registering...")
    try:
      firebase_Signup=self.auth.create_user_with_email_and_password(email_address, password)
    except:
      # Debug
      print("Email Already Exists!")
      return
    return