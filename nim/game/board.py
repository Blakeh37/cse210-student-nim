import random

class Board:
    
    def __init__(self):
        #list of numbers
        self.piles = {}
        self.__prepare()

    def __prepare(self):
        #turned the piles into a dictionary for better use 
        self.num_piles = random.randint(2,5)
        for pile in range(self.num_piles):
            num_stones = random.randint(1,9)
            stones = ('O ' * num_stones).split()
            self.piles[pile] = stones

    def to_string(self):
        text = ''
        for key in range(self.num_piles):
            Os = ' '.join(self.piles[key])
            text += (f'\n{key}: {Os}')
        return text

    def apply(self, move):
        #change the board based on the move 
        pile = move.get_pile()
        stones = move.get_stones()

        for i in range(stones):
            self.piles[pile].pop()

    def is_empty(self):
        #checks if there is no more stones 
        win_check = False

        for key in range(self.num_piles):
            if 'O' in self.piles[key]:
                win_check = False
            else:
                win_check = True
        return win_check


