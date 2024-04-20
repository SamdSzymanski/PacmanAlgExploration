from algs.parse_level import parse
from random import shuffle

def bfs(graph, coords, target):
  bag = []
  bag.append([coords])
  marked = set()
  while len(bag) != 0:
    curr = bag.pop(0)
    marked.add(curr[-1])
    last = curr[-1]
    for neighbor in graph[last]:
      if neighbor == 'val' or neighbor in marked:
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

def bfs_all(graph, coords, target):
  bag = []
  bag.append([coords])
  marked = set()
  while len(bag) != 0:
    curr = bag.pop(0)
    marked.add(curr[-1])
    last = curr[-1]
    neighbors = list(graph[last].keys())
    shuffle(neighbors)
    for neighbor in neighbors:
      if neighbor == 'val' or neighbor in marked:
        continue
      if neighbor == target:
        curr.append(neighbor)
        dirs = []
        prev = curr.pop(0)
        for vertex in curr:
          dirs.append(graph[prev][vertex])
          prev = vertex
        return dirs
      bag.append(curr + [neighbor])
