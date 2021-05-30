import sys

def init(graph, start_node):
  dist = {}
  prevNode = {}
  for node in graph:
    dist[node] = sys.maxsize
    prevNode[node] = None
  dist[start_node] = 0
  return dist, prevNode


def bellman_ford(graph, start_node):
  dist, prevNode = init(graph, start_node)
  path = []
  cnt = 0
 
  while(cnt < len(graph) - 1):
   
    for node in graph:
    
      for next_node in graph[node]:
        
        if(dist[node] + graph[node][next_node] < dist[next_node]):
          dist[next_node] = dist[node] + graph[node][next_node]
          prevNode[next_node] = node
    cnt += 1
 
  for node in graph:
    path.append(get_path(prevNode, node, 'a'))
  return dist, path


def get_path(prevNode, start_node, end_node):
  path = []
 
  while(start_node is not end_node):
    path.append(start_node)
    start_node = prevNode[start_node]
  path.append(end_node)
  return path 


graph ={
  'a': {'b': 2, 'c': 3, 'd':4},
  'b': {'e':2, 'f':3},
  'c': {'h':1},
  'd': {'h':4, 'g':2},
  'e': {'f':7},
  'f': {'g':4},
  'g': {'h':3},
  'h': {},
  }

distance, path = bellman_ford(graph, 'a')
toplam=0

print('Başlangıç Düğüm a:')
print('Düğüm | Maliyeti')
print('------|---------') 
for dist in distance:
  print('  %s   |  %d  ' % (dist , distance[dist]))
print('-----------------')

for dist in distance:
  toplam+=distance[dist]
print('Toplam Maliyeti:',toplam)

print('-----------------')
print()

print('Dokunduğu Düğümler:')
print('------|---------')
for nodes in path:
  if(len(nodes) != 1):
    print('  %s   |   a , %s' % (nodes[0], nodes[len(nodes) - 2]))
