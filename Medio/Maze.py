import os

import readchar

import random

xx = 0
yy = 1
Map_Width = 20
Map_Height = 20

NUMBER_OBSTACLES = 5

my_position = [6, 7]

map_objects = []

##for i in range(NUMBER_OBSTACLES):
##    map_objects.append([random.randint(0,20), random.randint(0,20)])
while len(map_objects) < NUMBER_OBSTACLES:
    new_position = [random.randint(0,20), random.randint(0,20)]
    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

while True:
    print("+" + "-" * Map_Height * 3 + "+")
    for y in range(Map_Height):
        print("|", end="")
        for x in range(Map_Width):
            char_to_draw = " "
            object_in_cell = None
            for map_object in map_objects:
                if map_object[xx] == x and map_object[yy] == y:
                    char_to_draw = "*"
                    object_in_cell= map_object
            if my_position[xx] == x and my_position[yy] == y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * Map_Height * 3 + "+")

    direction = readchar.readchar()
    print(direction)
    if direction == "w":
        my_position[yy] -= 1
        my_position[1] %= Map_Height
    elif direction == "s":
        my_position[yy] += 1
        my_position[1] %= Map_Height
    elif direction == "d":
        my_position[xx] += 1
        my_position[0] %= Map_Width
    elif direction == "a":
        my_position[xx] -= 1
        my_position[0] %= Map_Width
    elif direction == "q":
        break


    os.system("cls")

