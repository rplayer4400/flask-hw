from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Product(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    product_name=db.Column(db.String(50),nullable=False, unique=True)
    price=db.Column(db.Float(),nullable=False)
    image=db.Column(db.String())

    def __init__(self,product_name,price,image):
        self.product_name=product_name
        self.price=price
        self.image=image

class User(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
     email = db.Column(db.String(50), nullable=False, unique=True)
     password = db.Column(db.String(256), nullable=False)
    
     def __init__(self, username, email, password):
         self.email = email
         self.password = generate_password_hash(password)
         self.username = username
    
     def check_password(self, password):
         return check_password_hash(self.password, password)
