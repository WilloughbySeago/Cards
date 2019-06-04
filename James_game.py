"""This is a program to work out the probabilities involved with the game 'F*** the Bus'
The rules of this game are simple:
round 1 - guess red or black
round 2 - guess higher or lower than the previous card
round 3 - guess in or out of [1st card, 2nd card]
round 4 - guess the suit
If at any point you are wrong you must start from round 1 again
and drink as many times as the round you where wrong on"""

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
    global drinks
    result1 = round1(cards, 'red')
    if result1[0]:
        result2 = round2(cards, 'higher', result1[1])
    else:
        drinks += 1
        return False
    if result2[0]:
        result3 = round3(cards, 'out', result1[1], result2[1])
    else:
        drinks += 2
        return False
    if result3[0]:
        result4 = round4(cards, 's')
    else:
        drinks += 3
        return False
    if result4[0]:
        return True
    else:
        drinks += 4
        return False


attempts = 0
count = 0
drinks = 0
max_attempts = 1000000

while attempts < max_attempts:
    attempts += 1
    d = Deck()
    random.shuffle(d.deck)
    result = attempt(d)
    if result:
        count += 1

print(count)
print(count / max_attempts * 100)
print(drinks)
print(f'{round(drinks / (max_attempts - count), 4)} drinks per fail')
print(f'{round(drinks / max_attempts, 4)} drinks per attempt')


def good_strategy(cards):
    global drinks
    result1 = round1(cards, 'red')
    if result1[0]:
        card1 = result1[1]
        if get_val(card1) >= 8:
            high_low_guess = 'lower'
        else:
            high_low_guess = 'higher'
        result2 = round2(cards, high_low_guess, card1)
    else:
        drinks += 1
        return False
    if result2[0]:
        card2 = result2[1]
        cards_in_range = abs(get_val(card1) - get_val(card2)) - 1
        if cards_in_range >= 6:
            in_out_guess = 'in'
        else:
            in_out_guess = 'out'
        result3 = round3(cards, in_out_guess, card1, card2)
    else:
        drinks += 2
        return False
    if result3[0]:
        result4 = round4(cards, 's')
    else:
        drinks += 3
        return False
    if result4[0]:
        return True
    else:
        drinks += 4
        return False


attempts = 0
drinks = 0
count = 0

while attempts < max_attempts:
    attempts += 1
    d = Deck()
    random.shuffle(d.deck)
    result = attempt(d)
    if result:
        count += 1

print(count)
print(count / max_attempts * 100)
print(drinks)
print(f'{round(drinks / (max_attempts - count), 4)} drinks per fail')
print(f'{round(drinks / max_attempts, 4)} drinks per attempt')
