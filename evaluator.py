__author__ = 'rohit'
from itertools import groupby
from collections import Counter

# will hold logic for comparing players hands, see which hand is stronger according to poker rules
# uses logic from http://www.suffecool.net/poker/evaluator.html

# general algorithm: rank both hands according to hand type. if one hand is a better type than other, you have your winning hand. if both hands are same type, compare the kickers as needed for the hand type, and find winning hand.

# more general algorithm (naive): take in two hands of two cards each (player hands), and open cards (5 cards). 

# notes: the methods here have been written to handle find the best 5-card poker hand from a list of cards of arbitrarily length, i.e. these same functions should theoreticall support omaha and other similar poker games unchanged

# issues: will recognize flush and straight as straightflush even if they are seperate
STRAIGHT_FLUSH = 8
QUADS = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
TRIPLE = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

# 1 if hand 1 is better, -1 if hand 2 is better, 0 if equal
def determineWinningHand(hand1,hand2,openCards):
	# combine into two hands of 7 cards each
	handOne = hand1 + openCards
	handTwo = hand2 + openCards
	# sort for easy determining
	handOne.sort(key=lambda x:x.rank,reverse=True)
	handTwo.sort(key=lambda x:x.rank,reverse=True)
	# determine what the best hand is for each set of 7
	rankHandOne = evaluateHand(handOne)
	rankHandTwo = evaluateHand(handTwo)
	if rankHandOne > rankHandTwo:
		return 1
	elif rankHandOne < rankHandTwo:
		return -1
	else:
		return compareSameHand(handOne,handTwo)

# returns the ranking of the given hand (i.e. flush, straight, etc.) or -1 on error
def evaluateHand(hand):
	if isStraightFlush(hand):
		return STRAIGHT_FLUSH  
	elif isQuads(hand):
		return QUADS  
	elif isFullHouse(hand):
		return FULL_HOUSE  
	elif isFlush(hand):
		return FLUSH  
	elif isStraight(hand):
		return STRAIGHT  
	elif isTriple(hand):
		return TRIPLE  
	elif isTwoPair(hand):
		return TWO_PAIR  
	elif isPair(hand):
		return ONE_PAIR  
	else: # isHighCard(hand):
		return HIGH_CARD  
	return -1

# handOne and handTwo are both 7 cards
def compareSameHand(handOne,handTwo):
	return 1 # to be implemented later

# assumes a flush exists, will return most common suit by default
def getFlushCards(hand):
	suitList = [c.suit for c in hand]
	count = Counter(suitList)
	suitTuple = count.most_common(1)[0] # most common suit, and number of occurences
	return [c for c in hand if c.suit == suitTuple[0]] # all cards with the most common suit

def isStraightFlush(hand):
	if isFlush(hand):
		flushCards = getFlushCards(hand)
		return isStraight(flushCards)
	return False

def isQuads(hand):
	rankList = [c.rank for c in hand]
	count = Counter(rankList)
	rankTuple = count.most_common(1)[0] # most common rank, and number of occurences
	return rankTuple[1] == 4

def isFullHouse(hand):
	rankList = [c.rank for c in hand]
	count = Counter(rankList)
	rankTuples = count.most_common(2) 
	return (rankTuples[0][1] == 3) and (rankTuples[1][1] == 2)

def isFlush(hand):
	suitList = [c.suit for c in hand]
	count = Counter(suitList)
	suitTuple = count.most_common(1)[0] # most common suit, and number of occurences
	return suitTuple[1] >= 5

def isStraight(hand):
	rankList = [c.rank for c in hand]
	for i in range(2,11):
		# print set(range(i,i+5))
		# print set(rankList)
		if set(range(i,i+4)) <= set(rankList):
			return True
	return False

def isTriple(hand):
	rankList = [c.rank for c in hand]
	count = Counter(rankList)
	rankTuple = count.most_common(1)[0] # most common rank, and number of occurences
	return rankTuple[1] == 3

def isTwoPair(hand):
	rankList = [c.rank for c in hand]
	count = Counter(rankList)
	rankTuples = count.most_common(2) 
	return (rankTuples[0][1] == 2) and (rankTuples[1][1] == 2)

def isPair(hand):
	rankList = [c.rank for c in hand]
	count = Counter(rankList)
	rankTuple = count.most_common(1)[0] # most common rank, and number of occurences
	return rankTuple[1] == 2
