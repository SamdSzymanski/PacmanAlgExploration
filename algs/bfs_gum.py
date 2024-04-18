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
    graph, _ = parse(self.game.map, y, x)
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
    return self.game.pacman.direction


























'''def get_dir(self):
    if (self.game.pacman.y, self.game.pacman.x) in self.graph:
      if len(self.queue) != 0:
        direct = self.queue.pop(0)
        for edge in self.graph[(self.game.pacman.y, self.game.pacman.x)]:
          if self.graph[(self.game.pacman.y, self.game.pacman.x)][edge][0] == direct:
            temp = list(self.graph[(self.game.pacman.y, self.game.pacman.x)][edge])
            temp[1] = 0
            self.graph[(self.game.pacman.y, self.game.pacman.x)][edge] = tuple(temp)
            temp = list(self.graph[edge][(self.game.pacman.y, self.game.pacman.x)])
            temp[1] = 0
            self.graph[edge][(self.game.pacman.y, self.game.pacman.x)] = tuple(temp)
            self.graph[edge]['val'] = 0
            break
        return direct
      queue = []
      queue.append((self.game.pacman.y, self.game.pacman.x))
      paths = {}
      paths[(self.game.pacman.y, self.game.pacman.x)] = []
      while len(queue) != 0:
        curr = queue.pop(0)
        if self.graph[curr]['val'] == 1:
          self.queue = paths[curr]
          direct = self.queue.pop(0)
          for edge in self.graph[curr]:
            if edge == 'val':
              continue
            if self.graph[curr][edge][0] == direct:
              temp = list(self.graph[curr][edge])
              temp[1] = 0
              self.graph[curr][edge] = tuple(temp)
              temp = list(self.graph[edge][curr])
              temp[1] = 0
              self.graph[edge][curr] = tuple(temp)
              self.graph[edge]['val'] = 0
              break
          return direct
        for edge in self.graph[curr]:
          if edge == 'val':
            continue
          queue.append(edge)
          paths[edge] = paths[curr] + [self.graph[curr][edge][0]]
    return self.game.pacman.direction'''

# NEED TO CHANGE VALS FOR ALL TURNS