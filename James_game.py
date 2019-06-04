from Cards.Deck_class import *
import string
import random


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
    :param previous_card: Card
    :return: bool, Card
    """
    card = cards.deck.pop(0)
    card_val = str_to_int(card)
    prev_val = str_to_int(previous_card)
    if guess == 'higher' and card_val > prev_val:
        return True, card
    elif guess == 'lower' and card_val < prev_val:
        return True, card
    elif card_val == prev_val:
        print('same card')
        return round2(cards, guess, previous_card)
    elif guess == 'higher' and card_val < prev_val:
        return False, card
    elif guess == 'lower' and card_val > prev_val:
        return False, card


def str_to_int(card):
    val = card.value
    if val in string.digits or val == '10':
        val = int(val)
    elif val == 'j':
        val = 11
    elif val == 'q':
        val = 12
    elif val == 'k':
        val = 13
    else:
        val = 14
    return val
