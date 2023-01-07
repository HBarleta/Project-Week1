from flask import Flask
app = Flask(__name__)
app.secret_key = "Ninjas don't lie"
# secret key for session and flash
SHOPPINGCART = []
SHOPPINGTOTAL = 0
STRIPE_TOTAL = (SHOPPINGTOTAL * 100)
DATABASE = "takumis_garage" 
# global variable for schema


