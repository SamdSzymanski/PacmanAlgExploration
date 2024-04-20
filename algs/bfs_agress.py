from algs.parse_level import parse
from algs.p2p_bfs import bfs
from random import choice, shuffle

class BFS_Agress():

  game = None
  graph = None
  queue = []
  targets = []
  chasing = False

  def setup(self):
    self.targets = [(23, 1), (23, 26), (1, 1), (1, 26)]
    self.graph, _ = parse(self.game.map, self.game.pacman.y, self.game.pacman.x)
    temp = []
    for coord in self.targets:
      if self.graph[coord]['val'] == 1:
        temp.append(coord)
    self.targets = temp
    print('BFS_Agress ready')
  
  def get_dir(self):
    if (self.game.pacman.y, self.game.pacman.x) in self.targets:
      self.targets.remove((self.game.pacman.y, self.game.pacman.x))
    if (self.game.pacman.y , self.game.pacman.x) not in self.graph:
      return self.game.pacman.direction
    if len(self.queue) != 0:
      if self.game.pacman.mode == 'chase':
        if self.chasing:
          return self.queue.pop(0)
        for ghost in self.game.Ghosts:
          if (ghost.y, ghost.x) in self.graph:
            self.queue = bfs(self.graph, (self.game.pacman.y, self.game.pacman.x), (ghost.y, ghost.x))
            self.chasing = True
      self.chasing = False
      return self.queue.pop(0)
    if self.game.pacman.mode == 'chase':
      ghosts = self.game.Ghosts
      shuffle(ghosts)
      for ghost in ghosts:
        if (ghost.y, ghost.x) in self.graph:
          self.queue = bfs(self.graph, (self.game.pacman.y, self.game.pacman.x), (ghost.y, ghost.x))
          self.chasing = True
          return self.queue.pop(0)
    if len(self.targets) != 0:
      target = self.targets[0]
      self.queue = bfs(self.graph, (self.game.pacman.y, self.game.pacman.x), target)
      return self.queue.pop(0)
    self.chasing = False
    target = choice(list(self.graph.keys()))
    self.queue = bfs(self.graph, (self.game.pacman.y, self.game.pacman.x), target)
    return self.queue.pop(0)
    
    