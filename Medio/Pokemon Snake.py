

import readchar

import random

import os

barrera = """\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
x                                                                         x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
"""
my_position = [1, 1]
barrera = [list(row) for row in barrera.split("\n")]
Map_Width = len(barrera[0])  # ancho de mapa
Map_Height = len(barrera)  # largo



xx = 0
yy = 1
#Map_Width = 20
#Map_Height = 20

tail_length = 0
tail = []


map_objects = []
map_hp = []

end_game = False
died = False


print("Estas jugando mi version de Pokemon Snake")
difficulty =input("Elija la dificultad [1]Facil [2]Normal [3]Dificil [4]Infinito (Cambiara el numero de entrenadores y la vida de los peronajes)")
if difficulty == "1":
    NUMBER_OBSTACLES = 2
    NUMBER_HPS = 5
    infinito = -1
if difficulty == "2":
    NUMBER_OBSTACLES = 5
    NUMBER_HPS = 4
    infinito = -1
if difficulty == "3":
    NUMBER_OBSTACLES = 7
    NUMBER_HPS = 2
    infinito = -1
if difficulty == "4":
    NUMBER_OBSTACLES = 7
    NUMBER_HPS = 2
    infinito = 7

os.system("cls")

##poner el while fuera hace que antes de empezar el juego se generan en cambio dentro mientras se generan se rellena
while not end_game:
    while len(map_objects) < NUMBER_OBSTACLES:
        new_position = [random.randint(0,Map_Width-1 ), random.randint(0,Map_Height-1)]
        if new_position not in map_objects and new_position != my_position and \
            barrera[new_position[1]][new_position[0]] != "x":
              map_objects.append(new_position)
        while len(map_hp) <= NUMBER_HPS:
            position_hp = [random.randint(0, Map_Width - 1), random.randint(0, Map_Height - 1)]
            if position_hp not in map_hp and position_hp != my_position and \
                    barrera[position_hp[1]][position_hp[0]] != "x" and new_position[1] != position_hp \
                    and position_hp[0] != new_position[0]:
                map_hp.append(position_hp)

    os.system("cls")
    print("+" + "-" * Map_Width + "+")
    for y in range(Map_Height):
        print("|", end="")
        for x in range(Map_Width):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            hp_in_cell = None
            for map_object in map_objects:
                if map_object[xx] == x and map_object[yy] == y:
                    char_to_draw = "*"
                    object_in_cell= map_object
                    NUMBER_OBSTACLES = infinito
            for map_hps in map_hp:
                if map_hps[0] == x and map_hps[1] == y:
                    char_to_draw ="H"
                    hp_in_cell = map_hps
                    NUMBER_HPS = -1
            for tail_piece in tail:
                if tail_piece[xx] == x and tail_piece[yy] == y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[xx] == x and my_position[yy] == y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if hp_in_cell:
                    map_hp.remove(hp_in_cell)

                if tail_in_cell:
                    print("Has muerto")
                    end_game = True
                    died =  True
            if barrera[y][x] == "x":
                char_to_draw = "x"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (Map_Width ) + "+")

    print("Tamaño de la cola es {} ".format(tail_length))
    print("La cola es {} ".format(tail))
    direction = readchar.readchar()
    print(direction)

    new_position=None
    if direction == "w":
        new_position =[my_position[0], (my_position[1] -1) % Map_Width]

    elif direction == "s":
        new_position = [my_position[0], (my_position[1] + 1) % Map_Width]

    elif direction == "d":
        new_position = [(my_position[0] +1) % Map_Width, my_position[1]]

    elif direction == "a":
        new_position = [(my_position[0] -1) % Map_Width, my_position[1]]

    elif direction == "q":
        break
    if new_position:
        if  barrera[new_position[1]][new_position[0]] != "x":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

if died:
    print("Game Over Perro")

