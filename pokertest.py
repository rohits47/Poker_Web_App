__author__ = 'rohit'

import unittest
from engine import Table

class MyTestCase(unittest.TestCase):
	def test_tableStartingState(self):
		table = Table()
		self.assertEqual(table.pot, 0)
		self.assertEqual(table.dealerPosition, 0)
		self.assertEqual(table.actionPosition, 0)
		self.assertEqual(table.round, 0)
		self.assertEqual(len(table.deck.deck), 52)


if __name__ == '__main__':
	unittest.main()
