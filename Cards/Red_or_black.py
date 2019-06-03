from Cards.Deck_class import *
import random
from scipy.stats import binom_test


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
max_trials = 1000000

# choosing randomly
rand_correct = 0
while trials <= max_trials:
    d = Deck()
    random.shuffle(d.deck)
    d.deck.pop(0)
    r = random.randint(0, 2)
    if r == 0:
        rand_guess = 'red'
    else:
        rand_guess = 'black'
    if red_or_black(d, rand_guess):
        rand_correct += 1
    trials += 1

print(rand_correct)

# choose opposite of first card's colour
trials = 0
strategic_correct = 0
while trials <= max_trials:
    d = Deck()
    random.shuffle(d.deck)
    first_card = d.deck.pop(0)
    if first_card.colour == 'red':
        strategic_guess = 'black'
    else:
        strategic_guess = 'red'
    if red_or_black(d, strategic_guess):
        strategic_correct += 1
    trials += 1

print(strategic_correct)

# analysis

# percent correct
rand_percent = rand_correct / max_trials * 100
strategic_percent = strategic_correct / max_trials * 100

print(f'{round(rand_percent, 3)}% of random guesses where correct')
print(f'{round(strategic_percent, 3)}% of strategic guesses where correct')

# statistical significance test
p = 0.05  # set significance level
prob = binom_test(strategic_correct, max_trials, 0.5, 'greater')  # calculate prob given null hypothesis
if p < prob:
    print(f'{round(prob, 4) * 100}% is the probability that this would occur with the null hypothesis '
          + f'so we accept the null hypothesis')
else:
    print(f'{round(prob, 4) * 100}% is the probability that this would occur with the null hypothesis '
          + f'so we reject the null hypothesis')
