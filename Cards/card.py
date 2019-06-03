class Card:
    def __init__(self, value, suit):
        """
        This is a class for a single playing card. It simply stores the information that is on a card
        :param value: A string containing the letter (lowercase) or number used to denote the value of a
        card eg. 'A', '5', 'Q'
        :param suit: A string containing the (lowercase) first letter of the suit ('s', 'c', 'h', 'd')
        """
        self.value = value
        self.suit = suit
        if self.suit in ['s', 'c']:
            self.colour = 'black'
        else:
            self.colour = 'red'

# test
