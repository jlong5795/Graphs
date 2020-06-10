"""
Nodes == Verts == Vertices == Vertexes

    The thing that stores the data

Nodes connected by Edges
    Edges can be directional

If a graph has directional edges, it's called a "directed graph".

Traversals
----------

Keep track of what nodes we've visited to avoid revisiting them

    * Visited flag
    * Hash Table
    * Set

Depth-First Traversal
---------------------
Push starting node onto the stack
While stack isn't empty:
    pop the node off the top of the stack
    if the node isn't visited:
        visit the node (do whatever you plan to do with it)

        mark node as visited
        push all of its neighbors onto the stack

Breadth-First Traversal
---------------------
Push starting node onto the queue
While queue isn't empty:
    pop the node off the top of the queue
    if the node isn't visited:
        visit the node (do whatever you plan to do with it)

        mark node as visited
        push all of its neighbors onto the queue

Graph Representations
---------------------

How we store the graph in memory

1. Adjacency matrix
2. Adjacency list

A matrix is a grid
(T = Connection)

    A   B   C   D   E   F   G
A
B           T
C       T                   T
D
E
F
G           T


"""


