from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from engine import Table,Deck,Player

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/poker.db'
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def index():
	d = Deck()
	return "This is the poker home page."

if __name__ == '__main__':
	app.run(debug=True)
