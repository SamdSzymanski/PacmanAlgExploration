def parse(level, y, x):
  dirs = {}
  pacgums = 0
  bound_bottom = len(level)
  bound_right = len(level[0])
  for row1 in range(1, bound_bottom - 1):
    for space1 in range(1, bound_right - 1):
      val1 = level[row1][space1]
      if ((val1 < 16) and (any([True for spot in [level[row1 - 1][space1], level[row1 + 1][space1]] if spot < 16]) and any([True for spot in [level[row1][space1 - 1], level[row1][space1 + 1]] if spot < 16]))) or ((row1 == y) and (space1 == x)):
        val1 = 1 if val1 > 0 else 0
        node1 = (row1, space1)
        dirs[node1] = {}
        dirs[node1]['val'] = val1
        pacgums += val1
        count = 0
        for row2 in range(1, row1)[ : : -1]:
          val2 = level[row2][space1]
          if val2 > 15:
            break
          node2 = (row2, space1)
          if node2 in dirs:
            dirs[node1][node2] = ('up', count)
            dirs[node2][node1] = ('down', count)
            pacgums += count
            break
          count += 1 if val2 > 0 else 0
        count = 0
        for space2 in range(1, space1)[ : : -1]:
          val2 = level[row1][space2]
          if val2 > 15:
            break
          node2 = (row1, space2)
          if node2 in dirs:
            dirs[node1][node2] = ('left', count)
            dirs[node2][node1] = ('right', count)
            pacgums += count
            break
          count += 1 if val2 > 0 else 0
        if level[row1 + 1][space1] == 15:
          for row2 in range(0, row1):
            node2 = (row2, space1)
            if node2 in dirs:
              dirs[node1][node2] = ('down', count)
              dirs[node2][node1] = ('up', count)
              break
        if level[row1][space1 + 1] == 15:
          for space2 in range(0, space1):
            node2 = (row1, space2)
            if node2 in dirs:
              dirs[node1][node2] = ('right', count)
              dirs[node2][node1] = ('left', count)
              break
  return dirs, pacgums

def parse_all(level):
  graph = {}
  for row in range(1, len(level) - 1):
    for space in range(len(level[0])):
      if level[row][space] < 16:
        graph[(row, space)] = {}
        graph[(row, space)]['val'] = 1 if level[row][space] > 0 else 0
        if (row - 1, space) in graph:
          graph[(row, space)][(row - 1, space)] = 'up'
          graph[(row - 1, space)][(row, space)] = 'down'
        if (row, space - 1) in graph:
          graph[(row, space)][(row, space - 1)] = 'left'
          graph[(row, space - 1)][(row, space)] = 'right'
  graph[(14, 0)][(14, 27)] = 'left'
  graph[(14, 27)][(14, 0)] = 'right'
  return graph

def map_2_str(level):
  return '  '.join([' '.join(map(str, inner)) for inner in level])