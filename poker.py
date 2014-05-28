from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy
from engine import Table,Deck,Player

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/poker.db'
db = SQLAlchemy(app)

table = Table()
table.addPlayer("computer1")
table.addPlayer("computer2")
table.addPlayer("computer3")
table.addPlayer("computer4")
table.addPlayer("computer5")


@app.route('/', methods=['POST', 'GET'])
def index():
	# if request.method == "POST":
		# return url_for('game',playerName=request.form['player_name'])
		# if 'new_hand' in request.form:
		# 	currPlayer = table.currentPlayers[-1] # add player with 
		# 	table.reset()
		# 	table.startHand()
		# 	for player in table.currentPlayers:
		# 		table.processPlayerAction(player,"call")
		# 	table.endBettingRound()
		# 	return render_template("game2.html",player=currPlayer,table=table)
		# if table.round == 0:
		# 	currPlayer = table.addPlayer(request.form['player']) # add player with given name
		# 	table.startHand()
		# 	for player in table.currentPlayers:
		# 		# if player.name not currPlayer.name:
		# 		table.processPlayerAction(player,"call")
		# 	table.endBettingRound()
		# 	return render_template("game.html",player=currPlayer,table=table)
		# if table.round == 1:
		# 	# return str(request.form) 
		# 	currPlayer = table.currentPlayers[-1] # add player with 
		# 	table.processPlayerAction(currPlayer,"raise",int(request.form['bet']))
		# 	table.showFlop()
		# 	for player in table.currentPlayers:
		# 		if player.name != currPlayer.name:
		# 			table.processComputerAction(player)
		# 	table.endBettingRound()
		# 	return render_template("game.html",player=currPlayer,table=table)
		# if table.round == 2:
		# 	currPlayer = table.currentPlayers[-1] # add player with 
		# 	table.processPlayerAction(currPlayer,"raise",int(request.form['bet']))
		# 	table.showTurn()
		# 	for player in table.currentPlayers:
		# 		if player.name != currPlayer.name:
		# 			table.processComputerAction(player)
		# 	table.endBettingRound()
		# 	return render_template("game.html",player=currPlayer,table=table)
		# if table.round == 3:
		# 	currPlayer = table.currentPlayers[-1] # add player with 
		# 	table.processPlayerAction(currPlayer,"raise",int(request.form['bet']))
		# 	table.showRiver()
		# 	for player in table.currentPlayers:
		# 		if player.name != currPlayer.name:
		# 			table.processComputerAction(player)
		# 	table.endBettingRound()
		# 	return render_template("game.html",player=currPlayer,table=table)
		# if table.round == 4:
		# 	currPlayer = table.currentPlayers[-1] # add player with 
		# 	name = table.endHand()
		# 	table.round += 1
		# 	# table.reset()
		# 	# table.startHand()
		# 	return render_template("game.html",player=currPlayer,table=table,winningPlayer=name)
	return render_template("index.html")

@app.route('/game', methods=['POST', 'GET'])
def game():
	if request.method == "POST":
		table.humanPlayer = table.addPlayer(request.form['player_name'])
		table.startHand()
		playerToAct = table.currentPlayers[table.actionPosition]
		return render_template("game2.html",player=table.humanPlayer,table=table,actionName=playerToAct.name,dealerName=table.currentPlayers[table.dealerPosition].name)
	# no changes, just general reloading page, no back-end action taken
	playerToAct = table.currentPlayers[table.actionPosition] if table.currentPlayers else None
	return render_template("game2.html",player=table.humanPlayer,table=table,actionName=playerToAct.name,dealerName=table.currentPlayers[table.dealerPosition].name)

@app.route('/reset', methods=['POST', 'GET'])
def reset():
	table.reset()
	table.startHand()
	playerToAct = table.currentPlayers[table.actionPosition] if table.currentPlayers else None
	return render_template("game2.html",player=table.humanPlayer,table=table,actionName=playerToAct.name,dealerName=table.currentPlayers[table.dealerPosition].name)

@app.route('/processComputer', methods=['POST', 'GET'])
def processComputer():
	table.processComputerAction(table.currentPlayers[table.actionPosition])
	playerToAct = table.currentPlayers[table.actionPosition] if table.currentPlayers else None
	return render_template("game2.html",player=table.humanPlayer,table=table,actionName=playerToAct.name,dealerName=table.currentPlayers[table.dealerPosition].name)

@app.route('/processPlayer', methods=['POST', 'GET'])
def processPlayer():
	table.processPlayerAction(table.humanPlayer,request.form['action'],int(request.form['bet_val']))
	playerToAct = table.currentPlayers[table.actionPosition] if table.currentPlayers else None
	return render_template("game2.html",player=table.humanPlayer,table=table,actionName=playerToAct.name,dealerName=table.currentPlayers[table.dealerPosition].name)

if __name__ == '__main__':
	app.run(debug=True)
