from random import randint

class Rand_Dir_Legal():

  game = None

  def setup(self):
    print('Rand_Dir_Legal ready')

  def get_dir(self):
    moves = self.game.pacman.allowed_moves
    return moves[randint(0, len(moves) - 1)]