from flask import Flask, render_template, redirect, request, session, url_for, jsonify, send_from_directory
# imports flask for flask actions
from flask_app.models import category_model
from flask_app.models import item_model
# this will import models into controller to convert raw DB data 
# USE the CLASS needed not the entire model file and 
# rename using proper naming convention
from flask_app import app
# imports init file from flask app
from flask import flash
from flask_app import SHOPPINGCART
from flask_app import SHOPPINGTOTAL
import os
from flask import Flask, render_template, request
import stripe
from flask_app import STRIPE_TOTAL


stripe.api_key = stripe_keys['secret_key']





@app.route('/categories/single_item/<int:id>')
def single_item(id):
    data = {
        'id' : id
    }
    single_item = item_model.item.get_by_id(data)
    image = single_item.imageurl
    return render_template('single_item.html', single_item=single_item, image=image)

@app.route('/single_item/add_cart/<int:id>', methods=['post'])
def add_single_item(id):
    global SHOPPINGCART
    data = {
        'id' : id
    }
    item = item_model.item.get_by_id(data)
    if 'cart' not in session:
        session['cart'] = [item.id]
    else:
        session['cart'] = item.id
    SHOPPINGCART.append(session['cart'])

    
    return redirect('/categories')

@app.route('/shopping_cart')
def show_shopping_cart():
    global STRIPE_TOTAL
    cart = SHOPPINGCART
    all_items = []
    SHOPPINGTOTAL= 0
    charge_total = STRIPE_TOTAL
    for item in cart:
        single_item = item_model.item.get_by_id({'id':item})
        all_items.append(single_item)
        SHOPPINGTOTAL += single_item.price
    return render_template('shopping_cart.html', cart=cart, all_items=all_items, total=SHOPPINGTOTAL, charge_total=charge_total)

@app.route('/shopping_cart/remove/<int:id>')
def shopping_cart_remove(id):
    SHOPPINGCART.remove(int(id))
    return redirect('/shopping_cart')



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/charge', methods=['POST'])
def charge():

    # Amount in cents
    amount = STRIPE_TOTAL

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount, key=stripe_keys['publishable_key'])