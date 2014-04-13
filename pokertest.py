__author__ = 'rohit'

import unittest
from engine import Table,Player,Deck

class PokerTestCase(unittest.TestCase):
	def setUp(self):
		self.table = Table()
		self.table.addPlayer("rohit")
		self.table.addPlayer("akhil")
		self.table.addPlayer("anshuman")
		self.table.addPlayer("suket")
	
	# def tearDown(self):
	# 	self.table = Table()

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
		self.table.currentPlayers[0].stack += 100 # alter player object
		self.table.addPlayer("ishan") # alter main list
		self.assertEqual(self.table.allPlayers[0],self.table.currentPlayers[0]) # make sure currentPlayers holds references
		self.assertNotEqual(self.table.allPlayers, self.table.currentPlayers)

	# verify that positions increment and overrun properly
	def test_incrementPosition(self):
		print "testing incrementPosition:"
		pos = 3
		pos = self.table.incrementPosition(pos,6)
		self.assertEqual(pos,4)
		pos = 3
		pos = self.table.incrementPosition(pos,4) # should rollover to beginning index
		self.assertEqual(pos,0)

	# verify that hand starts in appropriate state for players and hands
	# tests table.startHand()
	def test_handStartConditions(self):
		pass

	# test that betting continues and ends properly in all scenarios (folds all around, check all around, raise all around, and all combinations thereof)
	# tests table.processPlayerAction() over multiple players
	def test_roundBetting(self):
		pass

	# verify that player's actions are processed appropriately
	# tests table.processPlayerAction internally
	def test_processPlayerAction(self):
		pass

	def test_fullHand(self):
		print self.table
		self.table.startHand()
		self.table.showFlop()
		print self.table

		


if __name__ == '__main__':
	unittest.main()
