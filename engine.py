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

	def getRandom(self):
		return self.deck.pop()

	def getHand(self):
		return [self.getRandom(),self.getRandom()]

	def getFlop(self):
		return [self.getRandom(),self.getRandom(),self.getRandom()]

	def reset(self):
		self.deck = []
		for rank in xrange(1,14): 
			for suit in xrange(1,5):
				self.deck.append(Card(rank,suit))
		random.shuffle(self.deck)


class Player:
	def __init__(self,name):
		self.name = name
		self.hand = []
		self.currentBet = 0
		self.lastAction = ""
		self.stack = 0


class Table:
	def __init__(self):
		# list of player objects playing at this table
		self.players = []
		self.deck = Deck()
		self.openCards = []
		self.pot = 0
		self.dealerPosition = 0
		self.actionPosition = 0
		self.bigBlind = 2
		self.minimumBuyin = 20
		self.maximumBuyin = 200

