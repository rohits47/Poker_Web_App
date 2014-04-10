import random

class Card:
	rankString = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
	suitString = ["clubs","diamonds","hearts","spades"]

	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit

	def __repr__(self):
		return self.rankString[self.rank-1] + " of " + self.suitString[self.suit-1]


class Deck:
	def __init__(self):
		self.reset()

	def __repr__(self):
		return ', '.join(str(c) for c in self.deck)

	def getCard(self):
		return self.deck.pop()

	def reset(self):
		self.deck = []
		for rank in xrange(1,14):
			for suit in xrange(1,5):
				self.deck.append(Card(rank,suit))
		random.shuffle(self.deck)


# player at a table, doesn't include database level info such as passwords, etc.
class Player:
	def __init__(self,name):
		self.name = name
		self.hand = []
		self.currentBet = 0
		# last action is check, raise, call, fold, or empty if first round
		self.lastAction = ""
		self.stack = 0

	def setHand(self,hand):
		self.hand = hand


# the "engine" that drives the game, handles all other model objects
class Table:
	def __init__(self):
		# list of player objects playing at this table
		self.players = []
		self.waitingPlayers = []
		self.deck = Deck()
		self.openCards = []
		self.pot = 0
		self.dealerPosition = 0 # index in the player array
		self.actionPosition = 0 # index in the player array
		self.round = 0 # the current round of betting (0=preflop,1 = preturn,2=preriver,3=postriver)
		self.bigBlind = 2 # amount to be posted for big blind
		self.minimumBuyin = 20
		self.maximumBuyin = 200

	def addPlayer(self,player):
		self.players.append(player)

	def dealHands(self):
		for player in self.players:
			player.setHand(self.deck.getCard(),self.deck.getCard())

	def runRoundOfBetting(self):
		pass
		# prompt player starting with person past big blind

	def promptPlayerForAction(self,player):
		pass

	def runTable(self):
		if len(players) > 2:
			# deal to all players
			# prompt each player to call, raise, or fold in order
			# after last person has checked/called/folded, flop and repeat

class HandComparator: # will hold logic for comparing players hands, see which hand is stronger according to poker rules
	pass