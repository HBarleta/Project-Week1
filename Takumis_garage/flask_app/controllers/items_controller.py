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


@app.route('/categories/single_item/<int:id>')
def single_item(id):
    data = {
        'id' : id
    }
    single_item = item_model.item.get_by_id(data)
    image = single_item.imageurl
    return render_template('single_item.html', single_item=single_item, image=image)
