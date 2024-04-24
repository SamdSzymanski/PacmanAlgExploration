from algs.parse_level import parse
from random import shuffle

class BFS_Gum():

  game = None
  queue = []

  def setup(self):
    print('BFS_Gum ready')
  
  def get_dir(self):
    y = self.game.pacman.y
    x = self.game.pacman.x
    graph, pacgums = parse(self.game.map, y, x)
    direction = self.game.pacman.direction
    if pacgums == 0:
      return direction
    coords = (y, x)
    if coords in graph:
      queue = self.queue
      if len(queue) != 0:
        return queue.pop(0)
      bag = []
      bag.append([coords])
      while len(bag) != 0:
        curr = bag.pop(0)
        last = curr[-1]
        keys = list(graph[last].keys())
        shuffle(keys)
        for neighbor in keys:
          if neighbor == 'val':
            continue
          if graph[last][neighbor][1] != 0 or graph[neighbor]['val'] == 1:
            curr.append(neighbor)
            dirs = []
            prev = curr.pop(0)
            for vertex in curr:
              dirs.append(graph[prev][vertex][0])
              prev = vertex
            queue = dirs
            return queue.pop(0)
          bag.append(curr + [neighbor])
    return direction