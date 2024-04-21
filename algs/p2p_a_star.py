from numpy import abs as absolute
import heapq

def manhattan_dist(start, target):
  return absolute(target[0] - start[0]) + absolute(target[1] - start[1])

def a_star(graph, start, target):
  queue = []
  preds = {}
  score = {}
  heapq.heappush(queue, [manhattan_dist(start, target), start])
  while len(queue) != 0:
    curr = heapq.heappop(queue)
    if curr[1] == target:
      path = [graph[preds[curr[1]]][curr[1]][0]]
      temp = preds[curr[1]]
      while temp != start:
        path.insert(0, graph[preds[temp]][temp][0])
        temp = preds[temp]
      return path
    for neighbor in graph[curr[1]]:
      if neighbor == 'val':
        continue
      if neighbor not in score:
        score[neighbor] = float('inf')
      temp = manhattan_dist(neighbor, target)
      if temp < score[neighbor]:
        preds[neighbor] = curr[1]
        score[neighbor] = temp
        assign = False
        for item in queue:
          if item[1] == neighbor:
            item[0] = temp
            assign = True
            break
        if assign:
          continue
        heapq.heappush(queue, [temp, neighbor])