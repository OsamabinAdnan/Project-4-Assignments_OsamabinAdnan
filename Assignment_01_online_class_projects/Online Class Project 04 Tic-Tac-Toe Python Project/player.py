import random

class Player:
    """Base class for all players"""
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        """Abstract method that should be implemented by all subclasses"""
        pass

class RandomComputerPlayer(Player):
    """Computer player that makes random moves"""
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    """Human player that takes input from console"""
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # Initialize variables for input validation
        valid_square = False
        val = None
        
        # Keep asking for input until a valid move is received
        while not valid_square:
            # Get player input
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we'll also say its invalid
            try:
                # Convert input to integer
                val = int(square)
                # Check if the move is available
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')
        
        # Return the validated move
        return val