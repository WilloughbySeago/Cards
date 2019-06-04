from Cards.Deck_class import *


def round1(cards, guess):
    """
    This function draws a card and then compares the colour to the guess
    :param cards: Deck
    :param guess: 'red' or 'black'
    :return: bool
    """
    card = cards.deck.pop(0)
    if card.colour == guess:
        return True
    else:
        return False
