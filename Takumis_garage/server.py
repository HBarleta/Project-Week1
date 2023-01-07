from flask_app import app
# import flask_app init file
from flask_app.controllers import items_controller
from flask_app.controllers import categories_controller
#import controller here
import os
import stripe


# DO NOT FORGET TO PIPENV INSTALL FLASK (server operations), 
# pyMySQL (connects to DB), pipenv install flask-bcrypt (password encryption)

if __name__=="__main__":
    app.run(debug=True, port=4242)