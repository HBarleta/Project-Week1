from flask import Flask
app = Flask(__name__)
app.secret_key = "Ninjas don't lie"
# secret key for session and flash

DATABASE = "takumis_garage" 
# global variable for schema