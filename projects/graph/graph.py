"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) # could add inverse to set a bi-directional edge
        else:
            raise IndexError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # create a set to store visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if that vertex has not been visited
            if v not in visited:
                # visit it (do the action)
                print(v)
                visited.add(v)

                # add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
        return visited

    def dft(self, starting_vertex):
        # create an empty queue and enqueue the starting vertex ID
        q = Stack()
        q.push(starting_vertex)

        # create a set to store visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.pop()

            # if that vertex has not been visited
            if v not in visited:
                # visit it (do the action)
                print(v)
                visited.add(v)

                # add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.push(next_vert)
        return visited
        

    def dft_recursive(self, starting_vertex, visited=set()):
        # see if the current node has been visited
        if starting_vertex not in visited:
            print(starting_vertex)
            # if not add it
            visited.add(starting_vertex)
            
            # find it's neighbors and call for each of them
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()

        q.enqueue([starting_vertex])

        while q.size() > 0:
            # remove first element which is a node in a list
            path = q.dequeue()
            # get the last element in that list
            last_vert = path[-1]
            print(last_vert)

            # if this is what we want, return it
            if last_vert == destination_vertex:
                return path
            
            # check neighbors 
            for neighbor in self.get_neighbors(last_vert):
                new_path = list(path)
                # add a path to the neighbors
                new_path.append(neighbor)
                print(new_path)
                q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        q = Stack()

        q.push([starting_vertex])

        while q.size() > 0:
            # remove first element which is a node in a list
            path = q.pop()
            # get the last element in that list
            last_vert = path[-1]
            print(last_vert)

            # if this is what we want, return it
            if last_vert == destination_vertex:
                return path
            
            # check neighbors 
            for neighbor in self.get_neighbors(last_vert):
                new_path = list(path)
                # add a path to the neighbors
                new_path.append(neighbor)
                print(new_path)
                q.push(new_path)
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[]):
        if starting_vertex == destination_vertex:
            return visited + [starting_vertex]
        else:
            visited.append(starting_vertex)
            
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    path = self.dfs_recursive(neighbor, destination_vertex, visited)

                    if path:
                        return path
            visited.remove(starting_vertex)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print(graph.bft(1))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
