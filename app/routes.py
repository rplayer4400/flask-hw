from app import app,db
from flask import render_template, redirect, url_for
from app.forms import Create_product, RegisterForm
from app.models import Product,User
from flask import flash

@app.route('/register', methods=['GET', 'POST'])
def register():
     form = RegisterForm()
     if form.validate_on_submit():

         username = form.username.data
         email = form.email.data
         password = form.password.data
         print(email, password)
         

         new_user = User(username,email, password)

         db.session.add(new_user)
         db.session.commit()

        
         flash(f'Thank you for signing up {new_user.username}!', 'danger')

        
         return redirect(url_for('index'))
     return render_template('register.html', title='Register for CT Blog', form=form)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create_product', methods = ['GET', 'POST' ])
def products():
    form = Create_product()
    if form.validate_on_submit():
        product_name= form.product_name.data
        price= form.price.data
        image= form.image.data

        new_product = Product (product_name,price,image)
        db.session.add(new_product)
        db.session.commit()
        my_products=Product.query.all()


    return render_template('create_products',product=my_products, hello=form)


        


        

    return render_template('create_product.html', hello=form)