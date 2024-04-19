from algs.parse_level import parse

def bfs(graph, coords, target):
  bag = []
  bag.append([coords])
  while len(bag) != 0:
    curr = bag.pop(0)
    last = curr[-1]
    for neighbor in graph[last]:
      if neighbor == 'val':
        continue
      if neighbor == target:
        curr.append(neighbor)
        dirs = []
        prev = curr.pop(0)
        for vertex in curr:
          dirs.append(graph[prev][vertex][0])
          prev = vertex
        return dirs
      bag.append(curr + [neighbor])
