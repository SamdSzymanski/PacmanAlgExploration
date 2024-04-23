from algs.parse_level import parse_all
from algs.p2p_a_star import a_star_all
from random import choice, shuffle

class A_Star_Agress():

  game = None
  graph = None
  queue = []
  targets = []

  def setup(self):
    self.queue = []
    self.targets = [(23, 1), (23, 26), (1, 1), (1, 26)]
    self.graph = parse_all(self.game.map)
    temp = []
    for coord in self.targets:
      if self.graph[coord]['val'] == 1:
        temp.append(coord)
    self.targets = temp
    print('A_Star_Agress ready')
  
  def get_dir(self):
    if len(self.queue) != 0:
      return self.queue.pop(0)
    if self.game.pacman.mode == 'chase':
      path = []
      for ghost in self.game.Ghosts:
        if (self.game.pacman.y, self.game.pacman.x) == (ghost.y, ghost.x):
          return self.game.pacman.direction
        temp = a_star_all(self.graph, (self.game.pacman.y, self.game.pacman.x), (ghost.y, ghost.x))
        if temp == None:
          continue
        if len(temp) < len(path) or path == []:
          path = temp
      self.queue = path
      return self.queue.pop(0)
    if len(self.targets) != 0:
      closest = []
      chosen = None
      for target in self.targets:
        path = a_star_all(self.graph, (self.game.pacman.y, self.game.pacman.x), target)
        if len(path) < len(closest) or closest == []:
          closest = path
          chosen = target
      self.queue = closest
      self.targets.remove(chosen)
      return self.queue.pop(0)
    target = choice(list(self.graph.keys()))
    self.queue = a_star_all(self.graph, (self.game.pacman.y, self.game.pacman.x), target)
    return self.queue.pop(0)