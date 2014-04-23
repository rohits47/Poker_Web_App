__author__ = 'rohit'

import unittest
from engine import Table,Player,Deck
import evaluator

class PokerTestCase(unittest.TestCase):
	def setUp(self):
		self.table = Table()
		self.table.addPlayer("rohit")
		self.table.addPlayer("opponent")
		self.deck = self.table.deck

	def test_straightFlush(self):
		print "test_straightFlush"
		hand = []
		opponentsHand = []
		# straight flush vs. straight flush
		hand.append(self.deck.getSpecificCard(1,1))
		hand.append(self.deck.getSpecificCard(13,1))
		opponentsHand.append(self.deck.getSpecificCard(9,1))
		opponentsHand.append(self.deck.getSpecificCard(8,1))
		openCards = []
		openCards.append(self.deck.getSpecificCard(12,1))
		openCards.append(self.deck.getSpecificCard(11,1))
		openCards.append(self.deck.getSpecificCard(10,1))
		openCards.append(self.deck.getSpecificCard(4,2)) # irrelevant card
		openCards.append(self.deck.getSpecificCard(3,2)) # irrelevant card
		print hand
		print opponentsHand
		print openCards
		self.table.allPlayers[0].hand = hand
		self.table.allPlayers[1].hand = opponentsHand

	def test_quads(self):
		print "test_quads"
		pass

	def test_fullHouse(self):
		print "test_fullHouse"
		pass

	def test_flush(self):
		print "test_flush"
		pass

	def test_straight(self):
		print "test_straight"
		pass

	def test_triple(self):
		print "test_triple"
		pass

	def test_twoPair(self):
		print "test_twoPair"
		pass

	def test_onePair(self):
		print "test_onePair"
		pass

	def test_highCard(self):
		print "test_highCard"
		pass


if __name__ == '__main__':
	unittest.main()
