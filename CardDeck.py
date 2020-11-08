from random import shuffle

class Card:
    def __init__(self, suit, value, symbol):
        self.suit = suit
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return "{} of {}".format(self.symbol, self.suit)

    def show(self):
        print("{} of {}".format(self.symbol, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        v_s = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"Jack": 10,"Queen": 10,"King": 10, "Ace":11}
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for sm, v in v_s.items(): 
                self.cards.append(Card(s, v, sm))

    def show(self):
        for c in  self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)
    
    def allCards(self, player):       
        self.cards +=  player.clearHand()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.show()

    def clearHand(self):
        clearHand = []
        for card in range(1, len(self.hand) + 1):
            clearHand.append(self.hand[len(self.hand) - 1])
            self.hand.pop()
        return clearHand
        
