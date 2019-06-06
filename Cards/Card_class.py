"""
This is a class for playing cards, each Card object contains value, suit and colour
"""


class Card:
    def __init__(self, value, suit):
        """
        This is a class for a single playing card. It simply stores the information that is on a card
        :param value: A string containing the letter (lowercase) or number used to denote the value of a
        card eg. 'A', '5', 'Q'
        :param suit: A string containing the (lowercase) first letter of the suit ('s', 'c', 'h', 'd')
        """
        self.value = value  # 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, k, a
        self.suit = suit  # s, c, d, h
        # assign colour
        if self.suit in ['s', 'c']:
            self.colour = 'black'
        else:
            self.colour = 'red'

    def show(self):
        """
        This prints a tuple of value and suit. Basically the information you would have if you held the card
        :return: None
        """
        print(self.value, self.suit)
