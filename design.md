# The process of designing and building a poker app in python

## Week 1
### Overall Design
The first thing to think about was the data representation. We have cards, decks, players, and tables (individual games) as the main data types. I initially considered representing cards as tuples of (rank,suit) and decks as lists of tuples and hands as lists of tuples, but this seemed ugly and the slight performance benefit over objects was not a concern. The larger goal of readability, clean design, and understandability was more important. So I settled on a Card object to hold the rank, suit, and a string lookup for convenient debugging to print what the card was. I also opted to keep the Deck as an object wrapper for the list of Cards, so as to have convenience methods for shuffling and dealing a random card while appropriately changing the state of the deck. The Player object should represent the state of a player at a table, and as such should inclue what their name is, their current hand, their current stack size, their current bet (so as to be able to calculate what they need to add to call a re-raise), and their last action as a string for convenient printing to the GUI to indicate to the rest of the table. The Table object provides most of the necessary information to run the game, and after some consideration I decided it should actually also hold the business logic to run the game itself. Although I considered keeping the engine conceptually seperate as its own module, since Poker is a game of minimal computation during the majority of the game (majority of computation would be at showdown to determine hand strength, or if I wanted to dynamically assess hand strength as the hand progressed which is out of the current scope), most of the engine's job would be to gather data from the other models and essentially pass it to the table, which seemed to have minimal benefit over having the table query the objects it owns and update its own state. 

Now that the design was settled, the next thing to figure out was program flow. This seemed straightforward, but had a lot of parts, so I stubbed out methods for most of the major parts (pre-deal, pre-flop, each round of betting, post flop, main run loop, resetting state of table/players for each hand, etc.). This is where week 1 ended.

## Week 2

Turns out side pots are actually really hard, so I'm going to gloss over that for now and just say everything goes into the main pot, and best hand wins and gets the main pot.

Filled out all the stubbed functionality methods from last week. Changed a bit of the flow, since I realized that there's no way to have the main run loop yield to each player, process each player action, and then continue if this is a web app that requires user interaction client-side. Instead, each user action drives the back-end to process that action, and set the game state to accept the next user's action, and end and continue the next round at the appropriate state (like an FSM! might have been easier if I wrote it out like one...). The table starts and the table has an initial state, and once the minimum number of people join, the table starts "running" and keeps running as long as at least 2 people are sitting. The general format of each "loop" is:
- start hand (move dealer button, post blinds, deal hand)
- pre-flop betting
- flop
- pre-turn betting
- turn
- pre-river betting
- river
- river betting
- showdown
- end hand

### Showdown evaluator
The only computationally complex part of the app, the hand evaluator needs to be able to compare two 5-card hands on a scale from high card to straight flush. Some quick searching yielded http://www.suffecool.net/poker/evaluator.html, which gives an efficient way to map each card to a prime number, map each multiplication to a unique unordered 5-card hand (unordered is important since a straight can be in any order on the table). The evaluator has been written to accept hands of arbitrary length so as to be as general as possible, so the engine should be able to support games such as omaha easily with few modifications, if any.

## Week 3

Didn't finish the hand comparator last week, so I'm finishing that this week along with a proper working GUI. For the comparator, I think I'm gonna try test-driven development properly, both to see what it's like and because it's fairly straightforward with the comparator.

### Action processing

In the scope of these four weeks, the game will only support a single user and multiple AIs, but the general action-processing model should expand to support multiple users fairly easily. The only real difference is that a seperate function for processing AI actions exists, that randomly picks an action from the available legal actions. The processing flow for each hand:
- table starts hand (freeze current players, bet blinds, set action position to one past big blind, and deal cards)
- gui only lets action position respond with check, call, bet, etc.

## Week 4



future work:
- side pots
- antes
- omaha/multiple flops
- multiple runs
- stats (hands won, lost, best hand, largest pot, best laydown, etc.)