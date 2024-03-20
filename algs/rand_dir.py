from random import choice

class Rand_Dir():

  game = None

  def setup(self):
    print('Rand_Dir ready')

  def get_dir(self):
    return choice(['up', 'right', 'down', 'left'])
