import random
import copy

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
		self.deck = []
		self.reset()

	def __repr__(self):
		return ', '.join(str(c) for c in self.deck)

	def getCard(self):
		return self.deck.pop()

	def size(self):
		return len(self.deck)

	def reset(self):
		del self.deck[:] # clears the list
		for rank in xrange(1,14):
			for suit in xrange(1,5):
				self.deck.append(Card(rank,suit))
		random.shuffle(self.deck)


# player at a table, doesn't include database level info such as passwords, etc.
class Player:
	def __init__(self,name):
		self.name = name
		self.stack = 0
		self.hand = []
		self.currentBet = 0
		self.lastAction = "" # last action is check, raise, call, fold, or empty if first round

	def setHand(self,hand):
		self.hand = hand

	def reset(self):
		del self.hand[:] # throw away player's hand
		self.lastAction = ""
		self.currentBet = 0

	def __repr__(self):
		retlist = []
		retlist.append(self.name)
		retlist.append(str(self.hand))
		retlist.append("current bet: " + str(self.currentBet))
		retlist.append("last action: " + str(self.lastAction))
		retlist.append("stack: " + str(self.stack))
		return ', '.join(retlist)


# the "engine" that drives the game, handles all other model objects
class Table:
	def __init__(self):
		self.allPlayers = [] # list of all player objects playing at this table
		self.currentPlayers = [] # The players in the current hand
		self.deck = Deck()
		self.openCards = []
		self.pot = 0
		self.dealerPosition = 0 # index in the player array
		self.actionPosition = 0 # index in the player array
		self.round = 0 # the current round of betting (0=preflop,1 = preturn,2=preriver,3=postriver)
		self.bigBlind = 2 # amount to be posted for big blind
		self.minimumBuyin = 20
		self.maximumBuyin = 200

	def __repr__(self):
		retlist = []
		retlist.append("allPlayers: " + str(self.allPlayers))
		retlist.append("currentPlayers: " + str(self.currentPlayers))
		retlist.append("deck size: " + str(self.deck.size()))
		retlist.append("open cards: " + str(self.openCards))
		retlist.append("pot: " + str(self.pot))
		retlist.append("action postion: " + str(self.actionPosition))
		retlist.append("round: " + str(self.round))
		# retlist.append("" + str(self.bigBlind))
		# retlist.append("" + str(self.minimumBuyin))
		# retlist.append("" + str(self.maximumBuyin))
		return ', \n'.join(retlist)


	def addPlayer(self,player):
		self.allPlayers.append(player) # player will be dealt in next hand

	# rotate list so dealer is first position in list
	# def moveDealerPosition(self):
	# 	self.allPlayers.append(self.allPlayers.pop())

	# reset for new hand (increment dealer and blind positions)
	def reset(self):
		self.pot = 0
		self.round = 0
		del self.openCards[:]
		self.dealerPosition += 1
		if len(self.allPlayers) > 0:
			self.dealerPosition = self.dealerPosition % len(self.allPlayers)
		else:
			self.dealerPosition = 0
		self.actionPosition = 0
		self.deck.reset()
		for player in self.allPlayers:
			player.reset()
		self.setCurrentPlayers()
		# clear pot, clear hands, reset deck, reset players, reset positions

	def dealHands(self):
		for player in self.allPlayers:
			player.setHand(self.deck.getCard(),self.deck.getCard())

	def runRoundOfBetting(self):
		# prompt player starting with person past big blind
		# if player folds, remove from currentPlayers
		if self.round == 0:
			pass
			# start with person past big blind
		else:
			pass
			# start with small blind

	def promptPlayerForAction(self,player):
		pass

	# copies references to Players currently in allPlayers to a new list, currentPlayers
	def setCurrentPlayers(self):
		self.currentPlayers = copy.copy(self.allPlayers)

	def startHand(self):
		# pre-deal action: post blinds
		self.setCurrentPlayers() # set players for this hand

		pass

	def runTable(self):
		self.startHand()
		while len(self.allPlayers) > 1:
			self.dealHands()
			# prompt each player to call, raise, or fold in order
			self.runRoundOfBetting()
			# after last person has checked/called/folded, flop and repeat


class HandComparator: # will hold logic for comparing players hands, see which hand is stronger according to poker rules
	pass