from algs.parse_level import parse, map_2_str
from copy import deepcopy
import json

class BFS_Mod():

  PATH = 'algs/data/BFS_Mod.json'
  OPPOSITES = {
    'up' : 'down',
    'right' : 'left',
    'down' : 'up',
    'left' : 'right'
  }
  game = None
  graph = None
  queue = None

  def setup(self):
    data = {}
    y = self.game.pacman.y
    x = self.game.pacman.x
    level = self.game.map
    level_str = map_2_str(level)
    graph, pacgums = parse(level, y, x)
    self.graph = deepcopy(graph)
    with open(self.PATH) as file:
      data = json.load(file)
    if level_str in data:
      self.queue = data[level_str]
      return
    processing = {((), 0, (y, x), 0)}
    graph_list = [graph]
    while True:
      temp_set = set()
      temp_list = []
      for item in processing:
        for move in graph[item[2]]:
          if move == 'val':
            continue
          dupe = deepcopy(graph_list[item[3]])
          turns = item[0]
          turns_len = len(turns)
          curr = dupe[item[2]][move]
          curr_dir = curr[0]
          if (turns_len != 0) and (curr_dir == self.OPPOSITES[turns[turns_len - 1]]):
            continue
          temp_tuple = list(item)
          temp_tuple[0] = list(temp_tuple[0])
          temp_tuple[0] += [curr_dir]
          temp_tuple[1] += curr[1] + dupe[move]['val']
          if temp_tuple[1] == pacgums:
            data[level_str] = temp_tuple[0]
            with open(self.PATH, 'w') as file:
              json.dump(data, file, indent = 2)
            self.queue = temp_tuple[0]
            return
          temp_tuple[0] = tuple(temp_tuple[0])
          dupe[move]['val'] = 0
          dupe[item[2]][move] = (curr_dir, 0)
          dupe[move][item[2]] = (dupe[move][item[2]][0], 0)
          temp_tuple[2] = deepcopy(move)
          temp_list += [dupe]
          temp_tuple[3] = len(temp_list) - 1
          temp_set.add(tuple(temp_tuple))
      count = len(processing)
      processing = {item1 for item1 in temp_set if item1[1] >= (sum(item2[1] for item2 in processing) / count if count > 0 else 0)}
      graph_list = temp_list
  
  def get_dir(self):
    if (self.game.pacman.y, self.game.pacman.x) in self.graph:
      return self.queue.pop(0)
    return self.game.pacman.direction