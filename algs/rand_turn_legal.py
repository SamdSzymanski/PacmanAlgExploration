from random import choice

class Rand_Turn_Legal():
  
  game = None
  dirs = ['right', 'left']

  def setup(self):
    print('Rand_Turn ready')
  
  def get_dir(self):
    moves = self.game.pacman.allowed_moves
    direct = self.game.pacman.direction
    if self.dirs != moves:
      self.dirs = moves
      return choice(moves)
    if direct not in self.dirs:
      return choice(self.dirs)
    return direct
