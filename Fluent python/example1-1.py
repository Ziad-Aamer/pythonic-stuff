# __getitem__ importance

import collections

# Define a new data type that has only fields without functions 
# (similar to how struct is used in C++ for types that we only want to define it struture)
Card = collections.namedtuple(typename='Card', field_names=['rank', 'suit'])

sample_card7 = Card('7', 'diamonds')
print(sample_card7)

class FrenchDech:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # deck of one suit 2-10, Jack, Queen, King and Ace
    suits = 'spades diamond clubs hearts'.split()
    
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDech()
print(len(deck)) # As we defined __len__ method
print(deck[0]) # __getitem__ method

# Additionally, slicing, itrating, sorting, ... are possible now because of the __getitem__ mehtod
print(deck[12::13]) # Get the aces of suits
for card in deck:
    print(card)
    
# We can also use choice to get random card
from random import choice
print(f'random choice: {choice(deck)}')

