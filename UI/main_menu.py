import time
from tkinter import *
import sys

sys.path.insert(0, r"C:\Users\mitch\Documents\Github\IA2-TopTrumps\API")

from firebase_authentication import firebase_authentication

class main_menu():

    def selection_window(self):
        global selection_window
        window = Tk()
        window.geometry("320x250")
        window.title("Account Login | Top Trumps")

        Label(text="Welcome", bg="cyan", width="300", height="2", font=("Calibri, 13")).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=self.login_window).pack() 
        Label(text="").pack() 
        Button(text="Register", height="2", width="30", command=self.register_window).pack()

        window.mainloop()

    def register_window(self):
        
        self.register_window=Tk()
        self.register_window.title("Register")
        self.register_window.title("320x250")

        Label(self.register_window, text="Please enter details below", bg="blue").pack()
        Label(self.register_window, text="").pack()

        self.email_label=Label(self.register_window, text="Email * ")
        self.email_label.pack()
        self.email_field=Entry(self.register_window)
        self.email_field.pack()
        self.password_label=Label(self.register_window, text="Password * ")
        self.password_label.pack()
        self.password_field=Entry(self.register_window, show="*")
        self.password_field.pack()
        Label(self.register_window, text="").pack()


        def firebase(email_address, password):
            FirebaseAuthentication = firebase_authentication()
            print(email_address, password)
            try:
                FirebaseAuthentication.firebase_Signup(email_address, password)
                Label(self.register_window, text="Registration Success", fg="green", font=("calibri", 11)).pack()
            except:
                Label(self.register_window, text="Registration Failed", fg="red", font=("calibri", 11)).pack()           

        Button(self.register_window, text="Register", width=10, height=1, bg="green", command=lambda : (firebase(self.email_field.get(), self.password_field.get()))).pack()

    def login_window(self):
        self.login_window=Tk()
        self.login_window.title("Login")
        self.login_window.title("320x250")

        Label(self.login_window, text="Please enter details below", bg="blue").pack()
        Label(self.login_window, text="").pack()

        self.email_label=Label(self.login_window, text="Email * ")
        self.email_label.pack()
        self.email_field=Entry(self.login_window)
        self.email_field.pack()
        self.password_label=Label(self.login_window, text="Password * ")
        self.password_label.pack()
        self.password_field=Entry(self.login_window, show="*")
        self.password_field.pack()
        Label(self.login_window, text="").pack()


        def firebase(email_address, password):
            FirebaseAuthentication = firebase_authentication()
            print(email_address, password)
            try:
                FirebaseAuthentication.firebase_Login(email_address, password)
                Label(self.login_window, text="Login Success", fg="green", font=("calibri", 11)).pack()
            except:
                Label(self.login_window, text="Login Failed", fg="red", font=("calibri", 11)).pack()           

        Button(self.login_window, text="Login", width=10, height=1, bg="green", command=lambda : (firebase(self.email_field.get(), self.password_field.get()))).pack()



nigger = main_menu()

nigger.selection_window()