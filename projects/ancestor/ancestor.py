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
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) # could add inverse to set a bi-directional edge
        else:
            raise IndexError('Vertex does not exist')

    def get_parents(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    # loop through list
    for i in ancestors:
        parent = i[1]
        child = i[0]
        # create nodes
        g.add_vertex(parent)
        g.add_vertex(child)
        # add paths to parent and child
        g.add_edge(parent, child)
    
    # keep track of paths
    path_list = []
    # keep track of what is being traversed
    stack = Stack()

    # push on starting node
    stack.push([starting_node])
    # create to store which have been 'visited'
    visited = set()

    # loop until the stack is empty
    while stack.size() > 0:
        # pop off the first item
        path = stack.pop()
        cur_node = path[-1]
        # if the current node hasn't been visited yet
        if cur_node not in visited:
            # add it to the current path
            path_list.append(path)
            # add it to visited nodes
            visited.add(cur_node)
            # find each parent of the current node
            for parent in g.get_parents(cur_node):
                # make a copy of the current path
                new_path = list(path)
                # add the parent to the copy of the current path
                new_path.append(parent)
                # push the parent onto the stack
                stack.push(new_path)
     
    print(path_list)
    # case for having no parents
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
            i += 1
            j += 1
        return correct_list[-1]
        
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 8)