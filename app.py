import pymysql
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace with your actual RDS details
DB_USER = "admin"
DB_PASSWORD = "pAR*123Ul"
DB_HOST = "ecomparuldb.c4p844iic8bb.us-east-1.rds.amazonaws.com"
DB_NAME = "ecommerce_db"

'''# 🔹 Configure MySQL connection
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

##db = SQLAlchemy(app)

# 🔹 Define Product Model (Optional, if you use SQLAlchemy ORM)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)'''

# 🔹 Route to display products on homepage
@app.route('/')
def home():
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = connection.cursor()

    # Fetch all products
    cursor.execute("SELECT id, product_name, product_price, product_description FROM products")
    products = cursor.fetchall()

    connection.close()

    return render_template('index.html', products=products)

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)
