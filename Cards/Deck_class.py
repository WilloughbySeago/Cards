from Cards.Card_class import *


class Deck:
    def __init__(self):
        """
        This creates a standard deck of cards
        """
        self.deck = []
        for suit in ['s', 'c', 'h', 'd']:
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']:
                self.deck.append(Card(value, suit))
