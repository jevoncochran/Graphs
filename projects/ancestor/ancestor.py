class Stack:
    def __init__(self):
        self.storage = []

    def push(self, val):
        self.storage.append(val)

    def pop(self):
        if self.size() > 0:
            return self.storage.pop()
        else:
            return None

    def size(self):
        return len(self.storage)
        

class Graph:
    def __init__(self):
        self.verts = {}

    def add_vert(self, vert_id):
        self.verts[vert_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)

    def get_parents(self, vert_id):
        return self.verts[vert_id]

data = [(10, 1), (1, 3), (2, 3), (4, 5), (4, 8), (11, 8), (3, 6), (5, 6), (5, 7), (8,9)]

def earliest_ancestor(ancestors, starting_node):

    g = Graph()
    for i in ancestors:
        parent = i[0]
        child = i[1]
        g.add_vert(parent)
        g.add_vert(child)
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


    if len(path_list) == 1:
        return -1
    else:
        i = 0
        j = 1
        correct_list = []
        while j < len(path_list):
            if len(path_list[i]) == len(path_list[j]):
                if path_list[i][-1] < path_list[j][-1]:
                    correct_list = path_list[i]
                else:
                    correct_list = path_list[j]
            else:
                correct_list = path_list[j]
            i+=1
            j+=1
        return correct_list[-1]


# test_graph = Graph()
# test_graph.add_vert(6)
# test_graph.add_vert(3)
# test_graph.add_vert(5)
# test_graph.add_edge(6, 3)
# test_graph.add_edge(6, 5)
# print(test_graph.get_parents(6))

earliest_ancestor(data, 6)




    
    
        
        








        