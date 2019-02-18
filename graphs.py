from random import randrange

class Vertex: # stores some data
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0): # storing the edges to connected vertices and their weight
    self.edges[vertex] = weight 

  def get_edges(self): # adding a new edges to its collection(list)
    return list(self.edges.keys())
  
  
class Graph: # stores all the vertices
  def __init__(self, directed = False): # whether directed or undirected
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex): # adding a new vertex to its collection
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0): # adding a new edge between stored vertices
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex): # whether a path exist between stored vertices
    start = [start_vertex]
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False

  
def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)


def build_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  for v in range(len(vertices)):
    v_idx = randrange(0, len(vertices) - 1)
    v1 = vertices[v_idx]
    v_idx = randrange(0, len(vertices) - 1)
    v2 = vertices[v_idx]
    g.add_edge(v1, v2, randrange(1, 10))

  print_graph(g)

build_graph(False)
###
a connected to
=> f

b connected to
=> d

g connected to
No edges!

e connected to
=> c

c connected to
=> e
=> d

f connected to
=> a

d connected to
=> b
=> c
=> d

