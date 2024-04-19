from algs.parse_level import parse
from random import choice
from algs.p2p_bfs import bfs

class BFS_Rand():

  game = None
  graph = None
  queue = []

  def setup(self):
    self.graph, _ = parse(self.game.map, self.game.pacman.y, self.game.pacman.x)
    print('BFS_Rand ready')
  
  def get_dir(self):
    if len(self.queue) == 0:
      if (self.game.pacman.y, self.game.pacman.x) in self.graph:
        self.graph, _ = parse(self.game.map, self.game.pacman.y, self.game.pacman.x)
        target = choice(list(self.graph.keys()))
        self.queue = bfs(self.graph, (self.game.pacman.y, self.game.pacman.x), target)
        return self.queue.pop(0)
      return self.game.pacman.direction
    if (self.game.pacman.y, self.game.pacman.x) in self.graph:
      return self.queue.pop(0)
    return self.game.pacman.direction