import random
import copy
import evaluator
from itertools import izip

# known bugs: if dealer folds, doesn't properly put action on first person to dealer's left

class Card:
	# 14 is ace for comparison simplicity
	rankString = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
	suitString = ["clubs","diamonds","hearts","spades"]

	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit

	def __repr__(self):
		return self.rankString[self.rank-2] + " of " + self.suitString[self.suit]

	# so collections can operate on it
	def __hash__(self):
		return (self.rank*10) + self.suit

	def __cmp__(self,other):
		if self.rank > other.rank:
			return 1
		elif self.rank < other.rank:
			return -1
		else:
			return 0


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
		for rank in xrange(2,15):
			for suit in xrange(0,4):
				self.deck.append(Card(rank,suit))
		random.shuffle(self.deck)

	# the following methods are for testing only

	def getSpecificCard(self,rank,suit):
		card = [x for x in self.deck if x.rank == rank and x.suit == suit]
		return card[0] # only one card for the given rank + suit


# player at a table, doesn't include database level info such as passwords, etc.
class Player:
	def __init__(self,name,stack):
		self.name = name
		self.stack = stack
		self.hand = []
		self.currentBet = 0
		self.lastAction = "" # last action is check, raise, call, fold, or empty if first round

	def setHand(self,hand):
		self.hand = hand

	def makeBet(self,bet):
		if bet > self.stack:
			bet = self.stack
		self.stack -= bet
		self.currentBet += bet

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
		return ', '.join(retlist) + '\n'


# the "engine" that drives the game, handles all other model objects
class Table:
	def __init__(self):
		self.allPlayers = [] # list of all player objects playing at this table
		self.currentPlayers = [] # The players in the current hand
		self.deck = Deck()
		self.openCards = []
		self.pot = 0
		self.dealerPosition = 0 # index in the player array
		self.smallBlindPosition = 1
		self.bigBlindPosition = 2
		self.actionPosition = 0 # index in the player array
		self.round = 0 # the current round of betting (0=preflop,1 = preturn,2=preriver,3=postriver)
		self.bigBlind = 2 # amount to be posted for big blind
		self.previousBet = self.bigBlind
		self.minimumBuyin = 20
		self.maximumBuyin = 200
		self.humanPlayer = None
		self.currentRoundActorPosition = self.actionPosition
		self.winningPlayer = ""
		self.winningHand = []

	def __repr__(self):
		# return self.tableConcise()
		retlist = []
		retlist.append("allPlayers: " + str(self.allPlayers))
		retlist.append("currentPlayers: " + str(self.currentPlayers))
		retlist.append("deck size: " + str(self.deck.size()))
		retlist.append("open cards: " + str(self.openCards))
		retlist.append("pot: " + str(self.pot))
		retlist.append("dealer position: " + str(self.dealerPosition))
		retlist.append("action position: " + str(self.actionPosition))
		retlist.append("round: " + str(self.round))
		retlist.append("sb pos: " + str(self.smallBlindPosition))
		retlist.append("bb pos: " + str(self.bigBlindPosition))
		# retlist.append("" + str(self.minimumBuyin))
		# retlist.append("" + str(self.maximumBuyin))
		return ', \n'.join(retlist)

	def tableConcise(self):
		retlist = dict()
		for player in self.allPlayers:
			retlist[player.name] = player.hand
		# retlist["table: "] = self.openCards
		return str(retlist) + " table: " + str(self.openCards)

	def addPlayer(self,player):
		p = Player(player,self.maximumBuyin)
		self.allPlayers.append(p) # player will be dealt in next hand
		return p

	def getPlayer(self,playerName):
		player = [p for p in self.allPlayers if p.name == playerName]
		return p[0]

	def showFlop(self):
		self.openCards.append(self.deck.getCard())
		self.openCards.append(self.deck.getCard())
		self.openCards.append(self.deck.getCard())

	def showTurn(self):
		self.openCards.append(self.deck.getCard())

	def showRiver(self):
		self.openCards.append(self.deck.getCard())

	# rotate list so dealer is first position in list
	# def moveDealerPosition(self):
	# 	self.allPlayers.append(self.allPlayers.pop())

	# returns new position given position, when incrementing on a list of given length
	def incrementPosition(self,position,listLength):
		position += 1
		return position % listLength

	def incrementDealerPosition(self):
		self.dealerPosition = self.incrementPosition(self.dealerPosition,len(self.currentPlayers))
		self.smallBlindPosition = self.incrementPosition(self.smallBlindPosition,len(self.currentPlayers))
		self.bigBlindPosition = self.incrementPosition(self.bigBlindPosition,len(self.currentPlayers))


	# reset for new hand (increment dealer and blind positions, remove empty stack players)
	def reset(self):
		self.pot = 0
		self.round = 0
		del self.openCards[:] # clear open cards
		self.actionPosition = 0
		self.previousBet = self.bigBlind
		self.deck.reset()
		self.winningPlayer = ""
		self.winningHand = []
		self.allPlayers = [p for p in self.allPlayers if p.stack > 0] # remove empty stack players
		for player in self.allPlayers:
			player.reset()
		# set current players and dealer pos will be done at start of hand in case people join between hands
		# self.setCurrentPlayers() # deal in all players seated at table
		# self.incrementDealerPosition() # moves blinds appropriately
		# clear pot, clear hands, reset deck, reset players, reset positions

	def dealHands(self):
		for player in self.currentPlayers:
			player.setHand([self.deck.getCard(),self.deck.getCard()])

	# copies references to Players currently in allPlayers to a new list, currentPlayers. changes to player objects (i.e stack) are mirrored in the allPlayers list.
	def setCurrentPlayers(self):
		self.currentPlayers = copy.copy(self.allPlayers)

	def playerBet(self,player,bet):
		player.makeBet(bet)
		self.pot += bet

	# set players in hand, post small and big blind, deal cards, and set actionPosition. users will drive input to process actions in action order
	def startHand(self):
		self.setCurrentPlayers() # set players for this hand
		self.incrementDealerPosition() # move dealer for this hand
		self.playerBet(self.currentPlayers[self.smallBlindPosition],self.bigBlind/2)
		self.playerBet(self.currentPlayers[self.bigBlindPosition],self.bigBlind)
		self.dealHands()
		self.actionPosition = self.incrementPosition(self.bigBlindPosition,len(self.currentPlayers))
		self.currentRoundActorPosition = self.actionPosition

	# winning player gets pot, check if any player is now out of the hand/table and remove them from the table, and reset for next hand
	def endHand(self):
		winningPlayer = self.currentPlayers[0]
		while len(self.currentPlayers) > 1:
			# print self.currentPlayers
			winner = evaluator.determineWinningHand(winningPlayer.hand,self.currentPlayers[1].hand,self.openCards)
			if winner == 1:
				del self.currentPlayers[1] # remove losing player
			else:
				winningPlayer = self.currentPlayers[1]
				del self.currentPlayers[0] # remove losing player
		winningPlayer.stack += self.pot
		self.winningPlayer = winningPlayer.name
		self.winningHand = winningPlayer.hand
		self.actionPosition = 0
		self.dealerPosition = 0
		# self.reset() # cleanup state for next hand

	def endBettingRound(self):
		for player in self.currentPlayers:
			player.lastAction = "" # clears lastAction
			player.currentBet = 0
		self.previousBet = 0
		self.actionPosition = self.incrementPosition(self.dealerPosition,len(self.currentPlayers)) # action is on first person past dealer still in the pot
		self.currentRoundActorPosition = self.actionPosition
		self.round += 1 # increment round
		if self.round == 1:
			self.showFlop()
		elif self.round == 2:
			self.showTurn()
		elif self.round == 3:
			self.showRiver()
		elif self.round == 4:
			self.endHand()

	# optional bet parameter (if folding or calling, bet is optional)
	def processPlayerAction(self,player,action,bet = 0):
		player.lastAction = action # common no matter what the action is
		# bet = int(bet)
		if action == "fold":
			# don't change previousBet
			self.currentPlayers.remove(player)
			# don't change action position, just return
			return
		elif action == "call":
			# don't change previous bet
			bet = self.previousBet - player.currentBet
			self.playerBet(player,bet)
		elif action == "raise":
			self.playerBet(player,bet)
			self.previousBet += bet
			self.currentRoundActorPosition = self.currentPlayers.index(player)
		# elif action == "allin":
		# 	self.playerBet(player,player.stack)
		self.actionPosition = self.incrementPosition(self.actionPosition,len(self.currentPlayers))
		if (self.actionPosition == self.currentRoundActorPosition) and action != "raise":
			self.endBettingRound()

	def processComputerAction(self,player):
		actionList = ["fold",  "call",  "raise",  "check"]
		actionList.remove("raise")
		if self.previousBet == 0:
			actionList.remove("fold") # stupid to fold if no bet
			actionList.remove("call") # can't call no bet
		if self.previousBet > 0:
			actionList.remove("check") # can't check if there's a bet
			actionList.remove("fold")
		action = random.choice(actionList)
		player.lastAction = action # common no matter what the action is
		# bet = int(bet)
		if action == "fold":
			# don't change previousBet
			self.currentPlayers.remove(player)
			# don't change action position, just return
			return
		elif action == "call":
			# don't change previous bet
			bet = self.previousBet - player.currentBet
			self.playerBet(player,bet)
		elif action == "raise":
			bet = random.randrange(self.bigBlind,player.stack/4) # bet a random amount from big blind to a fourth of stack
			self.playerBet(player,bet)
			self.previousBet += bet
			self.currentRoundActorPosition = self.currentPlayers.index(player)
		# elif action == "allin":
		# 	self.playerBet(player,player.stack)
		self.actionPosition = self.incrementPosition(self.actionPosition,len(self.currentPlayers))
		if (self.actionPosition == self.currentRoundActorPosition) and action != "raise":
			self.endBettingRound()
		# check action has no action associated
