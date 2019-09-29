__author__ = 'rohit'

import unittest
from engine import Table, Player, Deck
import evaluator


class PokerTestCase(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.table.addPlayer("rohit")
        self.table.addPlayer("opponent")
        self.deck = self.table.deck
        # set high and low representatives of each type of hand
        self.hand = []
        self.opponentsHand = []

    def tearDown(self):
        del self.hand[:]
        del self.opponentsHand[:]

    def test_straightFlush(self):
        print("test_straightFlush")
        # straight flush vs. straight flush
        openCards = []
        openCards.append(self.deck.getSpecificCard(11, 1))
        openCards.append(self.deck.getSpecificCard(12, 1))
        openCards.append(self.deck.getSpecificCard(10, 1))
        openCards.append(self.deck.getSpecificCard(4, 2))  # irrelevant card
        openCards.append(self.deck.getSpecificCard(3, 2))  # irrelevant card
        self.hand.append(self.deck.getSpecificCard(14, 1))
        self.hand.append(self.deck.getSpecificCard(13, 1))
        self.opponentsHand.append(self.deck.getSpecificCard(9, 2))
        self.opponentsHand.append(self.deck.getSpecificCard(8, 2))
        self.assertTrue(evaluator.isFlush(openCards + self.hand))
        self.assertTrue(evaluator.isStraightFlush(openCards + self.hand))
        self.assertEqual(
            evaluator.determineWinningHand(self.hand, self.opponentsHand,
                                           openCards), 1)
        # print self.hand
        # print self.opponentsHand
        # print openCards

    def test_quads(self):
        print("test_quads")
        openCards = []
        openCards.append(self.deck.getSpecificCard(9, 0))
        openCards.append(self.deck.getSpecificCard(9, 1))
        openCards.append(self.deck.getSpecificCard(10, 1))  # irrelevant card
        openCards.append(self.deck.getSpecificCard(4, 2))  # irrelevant card
        openCards.append(self.deck.getSpecificCard(3, 2))  # irrelevant card
        self.hand.append(self.deck.getSpecificCard(9, 2))
        self.hand.append(self.deck.getSpecificCard(9, 3))
        self.opponentsHand.append(self.deck.getSpecificCard(4, 2))
        self.opponentsHand.append(self.deck.getSpecificCard(4, 0))
        self.assertEqual(
            evaluator.determineWinningHand(self.hand, self.opponentsHand,
                                           openCards), 1)
        self.assertTrue(evaluator.isQuads(openCards + self.hand))

    def test_fullHouse(self):
        print("test_fullHouse")
        openCards = []
        openCards.append(self.deck.getSpecificCard(9, 0))
        openCards.append(self.deck.getSpecificCard(9, 1))
        openCards.append(self.deck.getSpecificCard(10, 1))
        openCards.append(self.deck.getSpecificCard(4, 2))  # irrelevant card
        openCards.append(self.deck.getSpecificCard(3, 2))  # irrelevant card
        self.hand.append(self.deck.getSpecificCard(9, 2))
        self.hand.append(self.deck.getSpecificCard(10, 3))
        self.opponentsHand.append(self.deck.getSpecificCard(2, 2))
        self.opponentsHand.append(self.deck.getSpecificCard(2, 0))
        self.assertEqual(
            evaluator.determineWinningHand(self.hand, self.opponentsHand,
                                           openCards), 1)
        self.assertTrue(evaluator.isFullHouse(openCards + self.hand))

    def test_flush(self):
        print("test_flush")
        openCards = []
        openCards.append(self.deck.getSpecificCard(3, 3))
        openCards.append(self.deck.getSpecificCard(7, 3))
        openCards.append(self.deck.getSpecificCard(10, 2))
        openCards.append(self.deck.getSpecificCard(8, 3))
        openCards.append(self.deck.getSpecificCard(13, 3))
        self.hand.append(self.deck.getSpecificCard(4, 2))
        self.hand.append(self.deck.getSpecificCard(10, 3))
        self.opponentsHand.append(self.deck.getSpecificCard(3, 2))
        self.opponentsHand.append(self.deck.getSpecificCard(7, 0))
        self.assertEqual(
            evaluator.determineWinningHand(self.hand, self.opponentsHand,
                                           openCards), 1)
        self.assertTrue(evaluator.isFlush(openCards + self.hand))

    def test_straight(self):
        print("test_straight")
        openCards = []
        openCards.append(self.deck.getSpecificCard(3, 1))
        openCards.append(self.deck.getSpecificCard(4, 1))
        openCards.append(self.deck.getSpecificCard(5, 2))
        openCards.append(self.deck.getSpecificCard(10, 0))
        openCards.append(self.deck.getSpecificCard(13, 3))
        self.hand.append(self.deck.getSpecificCard(6, 2))
        self.hand.append(self.deck.getSpecificCard(7, 3))
        self.opponentsHand.append(self.deck.getSpecificCard(7, 2))
        self.opponentsHand.append(self.deck.getSpecificCard(8, 0))
        self.assertEqual(
            evaluator.determineWinningHand(self.hand, self.opponentsHand,
                                           openCards), 1)
        self.assertTrue(evaluator.isStraight(openCards + self.hand))

    def test_triple(self):
        print("test_triple")
        openCards = []
        openCards.append(self.deck.getSpecificCard(3, 1))
        openCards.append(self.deck.getSpecificCard(4, 1))
        openCards.append(self.deck.getSpecificCard(5, 2))
        openCards.append(self.deck.getSpecificCard(10, 0))
        openCards.append(self.deck.getSpecificCard(13, 3))
        self.hand.append(self.deck.getSpecificCard(3, 2))
        self.hand.append(self.deck.getSpecificCard(5, 3))
        self.opponentsHand.append(self.deck.getSpecificCard(4, 2))
        self.opponentsHand.append(self.deck.getSpecificCard(4, 0))
        self.assertEqual(
            evaluator.determineWinningHand(self.hand, self.opponentsHand,
                                           openCards), -1)
        self.assertTrue(evaluator.isTriple(openCards + self.opponentsHand))

    def test_twoPair(self):
        print("test_twoPair")
        openCards = []
        openCards.append(self.deck.getSpecificCard(3, 1))
        openCards.append(self.deck.getSpecificCard(4, 1))
        openCards.append(self.deck.getSpecificCard(5, 2))
        openCards.append(self.deck.getSpecificCard(10, 0))
        openCards.append(self.deck.getSpecificCard(13, 3))
        self.hand.append(self.deck.getSpecificCard(3, 2))
        self.hand.append(self.deck.getSpecificCard(5, 3))
        self.assertTrue(evaluator.isTwoPair(openCards + self.hand))

    def test_onePair(self):
        print("test_onePair")
        openCards = []
        openCards.append(self.deck.getSpecificCard(3, 1))
        openCards.append(self.deck.getSpecificCard(4, 1))
        openCards.append(self.deck.getSpecificCard(5, 2))
        openCards.append(self.deck.getSpecificCard(10, 0))
        openCards.append(self.deck.getSpecificCard(13, 3))
        self.hand.append(self.deck.getSpecificCard(11, 2))
        self.hand.append(self.deck.getSpecificCard(10, 3))
        self.assertTrue(evaluator.isPair(openCards + self.hand))

    def test_highCard(self):
        print("test_highCard")
        openCards = []
        openCards.append(self.deck.getSpecificCard(3, 1))
        openCards.append(self.deck.getSpecificCard(4, 1))
        openCards.append(self.deck.getSpecificCard(5, 2))
        openCards.append(self.deck.getSpecificCard(10, 0))
        openCards.append(self.deck.getSpecificCard(13, 3))
        self.hand.append(self.deck.getSpecificCard(14, 2))
        self.hand.append(self.deck.getSpecificCard(7, 3))

    def test_misc(self):
        print("test_misc")
        openCards = []
        openCards.append(self.deck.getSpecificCard(8, 1))
        openCards.append(self.deck.getSpecificCard(10, 3))
        openCards.append(self.deck.getSpecificCard(9, 2))
        openCards.append(self.deck.getSpecificCard(9, 3))
        openCards.append(self.deck.getSpecificCard(3, 3))
        self.hand.append(self.deck.getSpecificCard(14, 2))
        self.hand.append(self.deck.getSpecificCard(11, 3))
        self.opponentsHand.append(self.deck.getSpecificCard(6, 3))
        self.opponentsHand.append(self.deck.getSpecificCard(6, 2))
        # print self.hand
        # print self.opponentsHand
        # print openCards
        self.assertEqual(
            evaluator.determineWinningHand(self.hand, self.opponentsHand,
                                           openCards), -1)


if __name__ == '__main__':
    unittest.main()
