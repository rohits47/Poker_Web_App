from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from engine import Engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/poker.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
	engine = Engine()
	d = Deck()
	p1 = Player("rohit") 
	table1 = Table()
	lst = d.getHand()
	return str(lst) + str(len(d.deck))
	return "This is the poker home page."

if __name__ == '__main__':
	app.run(debug=True)
