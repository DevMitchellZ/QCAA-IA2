#authentication.py by Mitchell Zarb
import pyrebase

class firebase_authentication():

  def __init__(self):
    self.firebaseConfig = {
      "apiKey": "AIzaSyAfNGIj7JGdK3NZ22i496pkAvQrmvffVyA",
      "authDomain": "ia2-digitalsoltuions.firebaseapp.com",
      "databaseURL": "",
      "projectId": "ia2-digitalsoltuions",
      "storageBucket": "ia2-digitalsoltuions.appspot.com",
      "messagingSenderId": "1059336754959",
      "appId": "1:1059336754959:web:b9aa02ea8761cea2a0907a",
      "measurementId": "G-MBS44P89K1"
    };

    self.firebase=pyrebase.initialize_app(self.firebaseConfig)
    self.auth=self.firebase.auth()


  #Login Function
  def firebase_Login(self):
    print("Log In...")
    user_email=input("Enter Email: ")
    user_password=input("Enter Password: ")
    try:
      firebase_Login = self.auth.sign_in_with_email_and_password(user_email, user_password)
      print("Successfully Logged In! ")
      print(self.auth.get_account_info(firebase_Login['idToken']))
    except:
      print("Incorrect Email or Password; Try Again! ")
    return

  #SignUp Function
  def firebase_Signup(self):
    print("Sign Up...")
    user_email=input("Enter Email: ")
    user_password=input("Enter Password: ")
    try:
      firebase_Signup = self.auth.create_user_with_email_and_password(user_email, user_password)
      verify=input("Do you want to Login? [Y/N] ")
      if verify=='Y':
        self.firebase_Login()
    except:
      print("Email already Exists! ")
    return


niggers=firebase_authentication()

# Main Console UI [ OPTIONAL ]
client_ans=input("Are you a New User? [Y/N] ")

if client_ans=="N":
  niggers.firebase_Login()
elif client_ans=="Y":
  niggers.firebase_Signup()