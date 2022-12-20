from flask import Flask, render_template, redirect, request, session
# imports flask for flask actions
from flask_app.models import category_model
from flask_app.models import item_model
# this will import models into controller to convert raw DB data 
# USE the CLASS needed not the entire model file and 
# rename using proper naming convention
from flask_app import app
# imports init file from flask app
from flask import flash
# import flash for incorrect inputs

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/categories')
def shop_all_categories():
    all_categories = category_model.category.get_all()
    return render_template('/categories.html', all_categories=all_categories)

@app.route('/categories/single_category/<int:id>')
def single_category(id):
    data = {
        'id' : id
    }
    one_category = category_model.category.get_by_id(data)
    return render_template('single_category.html', one_category=one_category)

