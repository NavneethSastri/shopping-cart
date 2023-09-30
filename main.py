from flask import Flask, render_template

app = Flask(__name__)

products = [
	{"id": 1, "name": "Test1", "price": 10},
	{"id": 2, "name": "Test2", "price": 10},
	{"id": 3, "name": "Test3", "price": 10},
]

cart = []

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/addCart/<int:product_id>')
def addCart():
	cart.append(prodcut_id)
	return redirect(url_for('index'))


app.run(host='0.0.0.0', port=81)
