from algs.parse_level import parse
from algs.p2p_a_star import a_star
from random import choice

class A_Star_Rand():
  
  game = None
  graph = None
  queue = []

  def setup(self):
    self.graph, _ = parse(self.game.map, self.game.pacman.y, self.game.pacman.x)
    print('A* Rand ready')
  
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
          if target == 'val':
            target = coords
        self.queue = a_star(graph, coords, target)
        return self.queue.pop(0)
      return direction
    if coords in graph:
      return self.queue.pop(0)
    return direction