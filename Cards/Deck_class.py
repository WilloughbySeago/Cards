"""
This is a class for a deck of cards that will create a deck of 52 cards
"""
from Cards.Card_class import *


class Deck:
    def __init__(self):
        """
        This creates a standard deck of cards
        """
        self.deck = []  # deck is just an array of Card objects
        # create all 13 cards of each suit
        for suit in ['s', 'c', 'h', 'd']:
            # for each suit create each card for every possible value
            for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']:
                self.deck.append(Card(value, suit))
