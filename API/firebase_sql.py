import pyrebase

class firebase_sql():

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
    self.db=self.firebase.database()


  def write_db(self, uuid, token, data):
    try: 
      return
    except:
      return


  def read_db(self, uuid, token, data):
    return