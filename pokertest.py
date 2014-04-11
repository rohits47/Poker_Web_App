__author__ = 'rohit'

import unittest
from engine import Table,Player,Deck

class PokerTestCase(unittest.TestCase):
	def setUp(self):
		self.table = Table()
		self.table.addPlayer(Player("rohit"))
		self.table.addPlayer(Player("bhargava"))

	def tearDown(self):
		self.table.reset()

	# verify starting state of table/game
	def test_startingState(self):
		print "testing starting state:"
		self.assertEqual(self.table.pot, 0)
		self.assertEqual(self.table.dealerPosition, 0)
		self.assertEqual(self.table.actionPosition, 0)
		self.assertEqual(self.table.round, 0)
		self.assertEqual(len(self.table.deck.deck), 52)

	# verify that currentPlayers updates player objects correctly
	def test_currentPlayers(self):
		print "testing currentPlayers list:"
		self.table.setCurrentPlayers()
		self.assertEqual(self.table.allPlayers, self.table.currentPlayers)
		self.table.currentPlayers[0].stack = 100 # alter player object
		self.table.addPlayer(Player("ishan")) # alter main list
		self.assertEqual(self.table.allPlayers[0],self.table.currentPlayers[0]) # make sure currentPlayers holds references
		self.assertNotEqual(self.table.allPlayers, self.table.currentPlayers)

	# verify that table runs a game properly
	def test_runTable(self):
		print "testing runTable:"
		print self.table


if __name__ == '__main__':
	unittest.main()
