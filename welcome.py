from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/')
def welcome_home():
    return 'welcome home'

@app.route('/')
def welcome_back():
    return 'welcome back'
    

