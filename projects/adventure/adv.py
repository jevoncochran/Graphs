from room import Room
from player import Player
from world import World
from util import Stack

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
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n', 's', 's', 'w', 'w', 'e', 'e', 'e', 'e', 'w', 'w', 's', 's']
traversal_path = []
visited = {}

# reverse helper fn
def reverse(direction):
    if direction == 'n':
        return 's'
    if direction =='s':
        return 'n'
    if direction == 'w':
        return 'e'
    if direction == 'e':
        return 'w'

def mark_visited(cur_room, exits):
    visited[cur_room] = {}
    for direction in exits:
        visited[cur_room][direction] = '?'

def make_path(cur_room):
    cur_room = player.current_room.id
    cur_exits = player.current_room.get_exits()
    prev_room = None
    stack = Stack()

    stack.push([None, cur_room, prev_room, cur_exits])

    while len(visited) < len(room_graph):
        path = stack.pop()
        direction = path[0]
        cur_room = path[1]
        prev_room = path[2]
        cur_exits = path[3]

        if cur_room not in visited:
            mark_visited(cur_room, cur_exits)

        if direction is not None:
            visited[cur_room][reverse(direction)] = prev_room

        if prev_room is not None:
            visited[prev_room][direction] = cur_room

        for d in visited[cur_room].keys():
            if visited[cur_room][d] == '?':
                stack.push(path)
                prev_room = player.current_room.id
                player.travel(d)
                traversal_path.append(d)
                stack.push([d, player.current_room.id, prev_room, player.current_room.get_exits()])
                break

        if cur_room == player.current_room.id:
            player.travel(reverse(direction))
            traversal_path.append(reverse(direction))
            
make_path(player.current_room.id)

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
