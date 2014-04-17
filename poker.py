from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from engine import Table,Deck,Player

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/poker.db'
db = SQLAlchemy(app)

table = Table()
table.addPlayer("opponent1")
table.addPlayer("opponent2")
table.addPlayer("opponent3")
table.addPlayer("opponent4")
table.addPlayer("opponent5")
currPlayer = None

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "POST":
		if table.round == 0:
			currPlayer = table.addPlayer("player") # add player with given name
			table.startHand()
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
		if table.round == 1:
			currPlayer = table.addPlayer("player") # add player with 
			table.showFlop()
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
		if table.round == 2:
			currPlayer = table.addPlayer("player") # add player with 
			table.startHand()
			table.showFlop()
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
	return render_template("index.html")

@app.route('/game', methods=['POST', 'GET'])
def game():
	render_template("game.html")

if __name__ == '__main__':
	app.run(debug=True)
