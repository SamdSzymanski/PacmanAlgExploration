from random import choice

class Rand_Dir_Legal():

  game = None

  def setup(self):
    print('Rand_Dir_Legal ready')

  def get_dir(self):
    return choice(self.game.pacman.allowed_moves)