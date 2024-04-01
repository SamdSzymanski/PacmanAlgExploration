from random import choice

class Rand_Dir_Charge():

  OPPOSITES = {
    'up' : 'down',
    'right' : 'left',
    'down' : 'up',
    'left' : 'right'
  }
  game = None

  def setup(self):
    print('Rand_Dir_Charge ready')

  def get_dir(self):
    return choice([move for move in self.game.pacman.allowed_moves if move != self.OPPOSITES[self.game.pacman.direction]])