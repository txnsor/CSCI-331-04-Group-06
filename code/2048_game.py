# 2048 Model (to be used with a GUI view)
# Implemented by Marc Browning

import numpy as np
from enum import Enum
from random import randint

# TODO: add dependencies to requirements.txt

"""
The default size of the square grid in one direction.
"""
DEFAULT_SIZE = 4

"""
Enumeration for the direction of movement.
"""
class DIRECTION(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

"""
Generic wrapper for 2048 grid with methods for movement.
"""
class Game:
    def __init__(self):
        # init grid
        self.grid = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE])
    
    # helper functions

    def __merge(self):
        # left merge
        for row in self.grid:
            for i in range(len(row) - 1):
                # if there is an avaliable merge, merge
                if row[i] == row[i + 1] and row[i] != 0:
                    row[i] += row[i + 1]
                    row[i + 1] = 0

    def __move_tiles(self):
        # move to left of arr
        self.grid = np.array([
            np.concatenate([row[row != 0], np.zeros(np.sum(row == 0))])
            for row in self.grid
        ])

    """
    Make a 2048 move in a given direction
    """
    def move(self, dir : DIRECTION):

    # change any direction into a LEFT move
        match dir:
            case DIRECTION.RIGHT:
                # if RIGHT, reverse each row
                self.grid = np.fliplr(self.grid)
            case DIRECTION.UP:
                # if UP, transpose
                self.grid = self.grid.T
            case DIRECTION.DOWN:
                # if DOWN, transpose and then reverse
                self.grid = np.fliplr(self.grid.T)

        # MOVE -> MERGE -> MOVE guarantees things work properly
        self.__move_tiles()
        self.__merge()
        self.__move_tiles()

        # undo rearrangements
        match dir:
            case DIRECTION.RIGHT: self.grid = np.fliplr(self.grid)
            case DIRECTION.UP: self.grid = self.grid.T
            case DIRECTION.DOWN: self.grid = np.fliplr(self.grid).T

    """
    Randomly place a tile on the board.
    """
    def random_place_tile(self, value = 2):
        while True:
            row = randint(0, DEFAULT_SIZE - 1)
            col = randint(0, DEFAULT_SIZE - 1)
            if self.grid[row, col] == 0:
                self.grid[row, col] = value
                return
    
    """
    Current total score.

    TODO: possibly change this?
    """
    def score(self):
        res = 0
        for row in self.grid:
            for val in row:
                res += val
        return res 
    
    """
    Checks if the game is lost or not.

    TODO: determine whether this is needed.
    """
    def is_game_lost(self):
        for row in self.grid:
            for val in row:
                if (val == 0): return False
        return True


# testing

def main():
    game = Game()

    game.grid[2, 2] = 2
    game.grid[2, 1] = 2
    game.grid[1, 2] = 2

    print("before move")
    print(game.grid)
    game.move(DIRECTION.RIGHT)
    print("after move (RIGHT)")
    print(game.grid)
    game.random_place_tile()
    print("random tile placed")
    print(game.grid)
    print(f"isGameLost? : {game.is_game_lost()}")

if __name__ == "__main__": main()


