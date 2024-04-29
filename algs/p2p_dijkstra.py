import heapq

def dijkstra(graph, start, target):
  queue = []
  preds = {}
  score = {}
  heapq.heappush(queue, [0, start])
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
      temp = curr[0] + graph[curr[1]][neighbor][1]
      if neighbor not in score or temp < score[neighbor]:
        preds[neighbor] = curr[1]
        score[neighbor] = temp
        heapq.heappush(queue, [temp, neighbor])
      