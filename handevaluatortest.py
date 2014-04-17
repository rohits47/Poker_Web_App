__author__ = 'rohit'

import unittest
from engine import Table,Player,Deck,HandComparator

class PokerTestCase(unittest.TestCase):
	def setUp(self):
		self.table = Table()
		self.table.addPlayer("rohit")
		self.table.addPlayer("akhil")
		self.table.addPlayer("anshuman")
		self.table.addPlayer("suket")
		self.table.startHand()
		comparator = HandComparator()


if __name__ == '__main__':
	unittest.main()
