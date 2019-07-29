#!/usr/bin/python3

class AMGraph:
  """ Partial Graph ADT represented by an adjacency matrix.
      From this point on, the term 'adjacency matrix' is denoted 'AM'. """

  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """ Lightweight vertex structure for a graph. """
    __slots__ = '_element', '_label'

    def __init__(self, x, label="UNEXPLORED"):
      """ Do not call constructor directly. Use Graph's addVertex(). """
      self._element = x
      self._label = label

    def element(self):
      """Return element associated with this vertex."""
      return self._element

    def getLabel(self, label):
      """ Get label assigned to this vertex. """
      return self._label

    def setLabel(self, label):
      """ Set label after the vertex has been created. """
      self._label = label

    def __str__(self):
      """ Used when printing this object. """
      return str(self._element)

  #------------------------- nested Edge class -------------------------
  class Edge:
    """ Lightweight edge structure for a graph. """
    __slots__ = '_origin', '_destination', '_element', '_label'

    def __init__(self, u, v, label="UNEXPLORED"):
      """Do not call constructor directly. Use Graph's addEdge(). """
      self._origin = u
      self._destination = v
      self._element = x
      self._label = label

    def getLabel(self, label):
      """ Get label assigned to this edge. """
      return self._label

    def setLabel(self, label):
      """ Set label after the edge has been created. """
      self._label = label

    def endpoints(self):
      """ Return (u,v) tuple for vertices u and v. """
      return (self._origin, self._destination)

    def opposite(self, v):
      """ Return the vertex that is opposite v on this edge. """
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')

    def element(self):
      """ Return element associated with this edge. """
      return self._element

    def __str__(self):
      """ Used when printing this object. """
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)


  #------------------------- Graph methods -------------------------
  #__slots__ =    # A 2D list representing the AM
  # Implement this

  #-- c'tor
  def __init__(self, filename):
    # ... Implement this
    # Open the given file, create an AM of the size specified in the file
    # Read data from the file, and insert edges into the AM
    return

  #-- Public methods
  def vertexCount(self):
    """ Return the number of vertices in the graph. """
    # ... Implement this
    return 0


  def vertices(self):
    """ Return an iteration of all vertices of the graph. """
    # ... Implement this
    return []


  def edgeCount(self):
    """ Return the number of edges in the graph. """
    # ... Implement this
    return 0

  def edges(self):
    """ Return a set of all edges of the graph. """
    # ... Implement this
    return []


  def addEdge(self, v1, v2):
    """ Add the edge represented by vertices v1 and v2 to the AM. """
    # ... Implement this
    return


  def getEdge(self, v1, v2):
    """ Return the edge from v1 to v2, or None if not adjacent. """
    # ... Implement this
    return None


  def incidentEdges(self, v):
    """ Return a collection of all edges incident to vertex v in the graph. """
    # ... Implement this
    return []


def BFS(g, minlevel=1):
  # ... Implement this according to the algorithm from the class notes,
  # and with the extra restrictions mentioned in the assignment
  return


#-- Main method

g = AMGraph("stations.txt")

# Test various methods
print("Vertices:", g.vertexCount())
for v in g.vertices():
  print(v, end=' ')
print()

print("Edges:", g.edgeCount())
for e in g.edges():
  print(e, end=' ')
print()

# Implement the algorithm from the assignment (repeated BFS traversals, etc)
# ...
