from random import choice

class Rand_Dir_Charge():

  game = None
  opposites = {
    'up' : 'down',
    'right' : 'left',
    'down' : 'up',
    'left' : 'right'
  }

  def setup(self):
    print('Rand_Dir_Charge ready')

  def get_dir(self):
    return choice([move for move in self.game.pacman.allowed_moves if move != self.opposites[self.game.pacman.direction]])