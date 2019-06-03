from Cards.Deck_class import *
import random


def red_or_black(cards, guess):
    """
    This function takes a deck and a guess and draws the top card and compares its colour to the guess
    :param cards: Deck
    :param guess: 'red' or 'black'
    :return: bool
    """
    top_card = cards.deck.pop(0)
    if top_card.colour == guess:
        return True
    else:
        return False


trials = 0
max_trials = 10000

# choosing randomly
rand_correct = 0
while trials <= max_trials:
    d = Deck()
    random.shuffle(d.deck)
    r = random.randint(0, 2)
    if r == 0:
        rand_guess = 'red'
    else:
        rand_guess = 'black'
    if red_or_black(d, rand_guess):
        rand_correct += 1
    trials += 1

print(rand_correct)
