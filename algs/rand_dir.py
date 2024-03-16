from random import randint

class Rand_Dir():

  dirs = {
    0 : 'up',
    1 : 'right',
    2: 'down',
    3: 'left'
  }

  def setup(self):
    print('Rand_Dir ready')

  def get_dir(self):
    return self.dirs[randint(0, 3)]