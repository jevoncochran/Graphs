class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")
    def get_parents(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

data = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for i in ancestors:
        parent = i[0]
        child = i[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(child, parent)
    path_list = []
    stack = Stack()
    stack.push([starting_node])
    visited = set()
    while stack.size() > 0:
        path = stack.pop()
        cur_node = path[-1]
        if cur_node not in visited:
            # print(cur_node, path)
            path_list.append(path)
            visited.add(cur_node)
            for parent in g.get_parents(cur_node):
                new_path = list(path)
                new_path.append(parent)
                stack.push(new_path)
    print(path_list)

earliest_ancestor(data, 6)