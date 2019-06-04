from Cards.Deck_class import *
import string
import random


def get_val(card):
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
    card_val = get_val(card)
    prev_val = get_val(previous_card)
    if guess == 'higher' and card_val > prev_val:
        return True, card
    elif guess == 'lower' and card_val < prev_val:
        return True, card
    elif card_val == prev_val:
        return round2(cards, guess, previous_card)
    elif guess == 'higher' and card_val < prev_val:
        return False, card
    elif guess == 'lower' and card_val > prev_val:
        return False, card


def round3(cards, guess, card1, card2):
    """
    This function draws a card and then compares whether it is between two other cards and compares that to the guess
    :param cards: Deck
    :param guess: 'in' or 'out'
    :param card1: Card
    :param card2: Card
    :return: bool, Card
    """
    card = cards.deck.pop(0)
    card_val = get_val(card)
    card1_val = get_val(card1)
    card2_val = get_val(card2)
    if card_val > card1_val and card_val > card2_val:
        in_out = 'out'
    elif card_val < card1_val and card_val < card2_val:
        in_out = 'out'
    elif card1_val < card_val < card2_val:
        in_out = 'in'
    elif card2_val < card_val < card1_val:
        in_out = 'in'
    else:
        return round3(cards, guess, card1, card2)
    if guess == in_out:
        return True, card
    else:
        return False, card


def round4(cards, guess):
    """
    This function draws a card and compares its suit to a guess
    :param cards: Deck
    :param guess: 's', 'c', 'h' or 'd'
    :return: bool, Card
    """
    card = cards.deck.pop(0)
    if card.suit == guess:
        return True, card
    else:
        return False, card


def attempt(cards):
    result1 = round1(cards, 'red')
    if result1[0]:
        result2 = round2(cards, 'higher', result1[1])
        if result2[0]:
            result3 = round3(cards, 'out', result1[1], result2[1])
            if result3[0]:
                result4 = round4(cards, 's')
                if result4[0]:
                    return True
    return False


attempts = 0
count = 0
while attempts < 100000:
    attempts += 1
    d = Deck()
    random.shuffle(d.deck)
    if attempt(d):
        count += 1
print(count)
print(count/100000 * 100)
