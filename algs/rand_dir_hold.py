from random import choice

class Rand_Dir_Hold():

  game = None

  def setup(self):
    print('Rand_Dir_Hold ready')

  def get_dir(self):
    direct = self.game.pacman.direction
    if direct not in self.game.pacman.allowed_moves:
      return choice(['up', 'right', 'down', 'left'])
    return direct