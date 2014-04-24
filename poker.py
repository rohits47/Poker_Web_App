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



@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "POST":
		if 'new_hand' in request.form:
			currPlayer = table.currentPlayers[-1] # add player with 
			table.reset()
			table.startHand()
			for player in table.currentPlayers:
				table.processPlayerAction(player,"call")
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
		if table.round == 0:
			currPlayer = table.addPlayer(request.form['player']) # add player with given name
			table.startHand()
			for player in table.currentPlayers:
				# if player.name not currPlayer.name:
				table.processPlayerAction(player,"call")
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
		if table.round == 1:
			# return str(request.form) 
			currPlayer = table.currentPlayers[-1] # add player with 
			table.processPlayerAction(currPlayer,"raise",int(request.form['bet']))
			table.showFlop()
			for player in table.currentPlayers:
				if player.name != currPlayer.name:
					table.processComputerAction(player)
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
		if table.round == 2:
			currPlayer = table.currentPlayers[-1] # add player with 
			table.processPlayerAction(currPlayer,"raise",int(request.form['bet']))
			table.showTurn()
			for player in table.currentPlayers:
				if player.name != currPlayer.name:
					table.processComputerAction(player)
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
		if table.round == 3:
			currPlayer = table.currentPlayers[-1] # add player with 
			table.processPlayerAction(currPlayer,"raise",int(request.form['bet']))
			table.showRiver()
			for player in table.currentPlayers:
				if player.name != currPlayer.name:
					table.processComputerAction(player)
			table.endBettingRound()
			return render_template("game.html",player=currPlayer,table=table)
		if table.round == 4:
			currPlayer = table.currentPlayers[-1] # add player with 
			name = table.endHand()
			table.round += 1
			# table.reset()
			# table.startHand()
			return render_template("game.html",player=currPlayer,table=table,winningPlayer=name)
	return render_template("index.html")

@app.route('/game', methods=['POST', 'GET'])
def game():
	render_template("game.html")

if __name__ == '__main__':
	app.run(debug=True)
