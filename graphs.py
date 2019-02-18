class Vertex: # stores some data
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0): # storing the edges to connected vertices and their weight
    self.edges[vertex] = weight 

  def get_edges(self): # adding a new edges to its collection
    return self.edges.keys()
  
  
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
