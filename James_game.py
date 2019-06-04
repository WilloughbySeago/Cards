from Cards.Deck_class import *
import string


def round1(cards, guess):
    """
    This function draws a card and then compares the colour to the guess
    :param cards: Deck
    :param guess: 'red' or 'black'
    :return: bool, Card
    """
    card = cards.deck.pop(0)
    if card.colour == guess:
        return True, card
    else:
        return False, card


def round2(cards, guess, previous_card):
    """
    This function draws a card and then compares it to the guess of higher or lower
    :param cards: Deck
    :param guess: 'higher' or 'lower'
    :return: bool, Card
    """
    card = cards.deck.pop(0)
    if card.value in string.digits or card.value == '10':
        card_val = int(card.value)
    elif card.value == 'j':
        card_val = 11
    elif card.value == 'q':
        card_val = 12
    elif card.value == 'k':
        card_val = 13
    else:
        card_val = 14
    if guess == 'higher' and card_val > previous_card.value:
        return True, card
    elif guess == 'lower' and card_val < previous_card.value:
        return True, card
    elif card_val == previous_card.value:
        return round2(cards, guess, previous_card)

