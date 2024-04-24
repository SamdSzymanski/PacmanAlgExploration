#Code goes here
from algs.parse_level import parse

class DFS(self):
#Initialize the game state and the stack that will be sued to store all the nodes in the map
  game = None
  stack = [] 
  def setup(self):
    pass

  
  def get_dir(self):
    #Variables that will be used 
    y = self.game.pacman.y
    x = self.game.pacman.x
    graph = parse(self.game.map, y, x)
    direction = self.game.pacman.direction
    coords = (y,x)
    

    #Depth first search
    #Init an empty stack for storage of nodes
    stack = []
    n = len(stack)
    #For each vertex u, define u.visited to be false
    visited = set()
    #Push pacmans starting position into stack
    stack.push([coords])
    #While stack not empty
    while n != 0:
      #Pop the first element in S, u (called vertex)
      curr_vertex = stack.pop(n-1)
      visited.add(curr_vertex[-1])
      last = curr_vertex[-1]
      for neighbor in graph[last]:
        if neighbor == 'val' or neighbor in marked:
          continue
        if neighbor 
      #If u.visited = false:
      if vertex not in visited:
        #u.visited = true
        visited.add(vertex)
        #For each unvisited neighbor w of u:
        
        stack.extend(graph[vertex] - visited)
          #Push w into S
    #End search once all nodes are visited
return direction

#How do I implement this formula into a way that decides pacman directions?
#MUST return direction

      
      


