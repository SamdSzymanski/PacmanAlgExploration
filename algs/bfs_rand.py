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
    game = self.game
    pacman = game.pacman
    y = pacman.y
    x = pacman.x
    coords = (y, x)
    graph = self.graph
    direction = pacman.direction
    if len(self.queue) == 0:
      if coords in graph:
        graph, _ = parse(game.map, y, x)
        target = coords
        while target == coords:
          target = choice(list(graph.keys()))
        self.queue = bfs(graph, coords, target)
        return self.queue.pop(0)
      return direction
    if coords in graph:
      return self.queue.pop(0)
    return direction