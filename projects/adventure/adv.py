from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visted = {}
# keep track of how we got to our current location
path = []
# based on the entrance keep track of the way back out of the room the same way
possible_moves = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

visted[player.current_room.id] = player.current_room.get_exits()

# while we haven't visited all the rooms
while len(visted) < len(room_graph) -1:
    # if the current room hasn't been visited before
    if player.current_room.id not in visted:
        # add the current exits 
        visted[player.current_room.id] = player.current_room.get_exits()
        # keep track of the prev direction traveled (for backtracking)
        prev_direction = path[-1]
        # remove option because we've already been there
        visted[player.current_room.id].remove(prev_direction)
    
    # when you have no more exits that haven't been explored
    while len(visted[player.current_room.id]) == 0:
        # remove the last direction (being back tracking)
        prev_direction = path.pop()
        # record the room as you backtrack
        traversal_path.append(prev_direction)
        # move back
        player.travel(prev_direction)

    # set up for next loop
    # remove current room's unexplored directions
    next_move = visted[player.current_room.id].pop(0)
    # add to the traversal path
    traversal_path.append(next_move)
    # add to "how we got here"
    path.append(possible_moves[next_move])
    # actually move
    player.travel(next_move)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
