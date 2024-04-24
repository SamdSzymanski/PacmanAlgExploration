from random import choice

class Rand_Dir_Legal_Hold():

  game = None

  def setup(self):
    print('Rand_Dir_Legal_Hold ready')

  def get_dir(self):
    direct = self.game.pacman.direction
    moves = self.game.pacman.allowed_moves
    if direct not in moves:
      return choice(moves)
    return direct
