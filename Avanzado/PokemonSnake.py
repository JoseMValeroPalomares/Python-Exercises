

import readchar

import random

import os



#Aqui estan los ataques de cada pokemon
pokemon0 = ["Ascuas", "Placaje"]
pokemon1 = ["Burbujas", "Placaje"]
pokemon2 = ["Latigo zepa", "Bofetón"]
pokemon3 = ["Bola Voltio", "Impactrueno"]
pokemon4 = ["Placaje", "Canto"]
pokemon5 = ["Colmillo", "Embrujo"]
pokemon6 = ["Dormir", "Placaje"]
#Aqui definimos cuales son los pokemons
pokemons =["Charmander","Squirtle","Bulbasaur","Pikachu","Jigglypuff","Gengar","Snorlax"]


print("Estas jugando mi version de Pokemon Snake\n")
poke_player = None
#Aqui le preguntamos al jugador que pokemon quiere elegir
while poke_player !="0" and poke_player !="1" and poke_player !="2" and poke_player !="3" and poke_player !="4" and poke_player !="5" and poke_player !="6" and poke_player !="7" :
    poke_player = input(" \nElige tu pokemon (0)Charmander (1)Squirtle (2)Bulbasaur (3)Pikachu (4)Jigglypuff (5)Gengar (6)Snorlax ")
    if poke_player == "0":
        poke_player1 = pokemons[0]
        poke_player2 = pokemon0
        poke_player1_damage= [19,11]
        hp_poke = 90
        hp_poke_total = hp_poke
    elif poke_player== "1":
        poke_player1 = pokemons[1]
        poke_player2 = pokemon1
        poke_player1_damage = [15, 11]
        hp_poke = 95
        hp_poke_total = hp_poke
    elif poke_player == "2":
        poke_player1 = pokemons[2]
        poke_player2 = pokemon2
        poke_player1_damage = [14, 8]
        hp_poke = 105
        hp_poke_total = hp_poke
    elif poke_player== "3":
        poke_player1 = pokemons[3]
        poke_player2 = pokemon3
        poke_player1_damage = [18, 9]
        hp_poke = 90
        hp_poke_total = hp_poke
    elif poke_player == "4":
        poke_player1 = pokemons[4]
        poke_player2 = pokemon4
        poke_player1_damage = [6, 8]
        hp_poke = 125
        hp_poke_total = hp_poke
    elif poke_player == "5":
        poke_player1 = pokemons[5]
        poke_player2 = pokemon5
        poke_player1_damage = [10, 8]
        hp_poke = 125
        hp_poke_total = hp_poke
    elif poke_player == "6":
        poke_player1 = pokemons[6]
        poke_player2 = pokemon6
        poke_player1_damage = [-5, 8]
        hp_poke = 140
        hp_poke_total = hp_poke
    elif poke_player == "7": #pokemon oculto xD
        poke_player1 = pokemons[6]
        poke_player2 = pokemon6
        poke_player1_damage = [-5, 999]
        hp_poke = 400
        hp_poke_total = hp_poke
    else:
        print("Opcion invalida")

print(" \nTu pokemon es {} y Sus ataques son {} y {} \n".format(poke_player1, poke_player2[0], poke_player2[1]))

barrera = """\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x                                                                         x
x      xxxxxxx       xxxx             xxxxx         xx    xxxxxxx    xx   x
x                                                                         x
x              xxxxx          xxxxx                    xxxxxxxxx          x
x                                                                         x
x        xxxxxxx                       xxxxx                   xxxxxxx    x
x                          xx                                             x
x                            xx   xxxx                   xxxxxxx       xxxx
x                  xxxxx       xxxx                                       x
x                                 xxx                                     x
x                             xxxxxx                  xxxxx               x
x      xxxxxxxxx                                                  xxxxx   x
x                                                                         x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
"""
#posicion del jugador
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

#Dificultad lo que hace es cambiar el numero de curaciones y el numero de obstaculos
##Podria añadirle que dependiendo la dificultad la vida del rival tenga mas o menos vida y su ataque haga mas o menos daño
#Pero me da pereza asi que a lo mejor algun dia lo actualizo

difficulty = None
while difficulty !="1" and difficulty !="2" and difficulty !="3" and difficulty !="4":
    difficulty =input("Elija la dificultad [1]Facil [2]Normal [3]Dificil [4]Infinito (Cambiara el numero de entrenadores y la vida de los peronajes)")
    if difficulty == "1":
        NUMBER_OBSTACLES = 2
        NUMBER_HPS = 5
        infinito = -1
    if difficulty == "2":
        NUMBER_OBSTACLES = 4
        NUMBER_HPS = 4
        infinito = -1
    if difficulty == "3":
        NUMBER_OBSTACLES = 7
        NUMBER_HPS = 3
        infinito = -1
    if difficulty == "4":
        NUMBER_OBSTACLES = 1
        NUMBER_HPS = 3
        infinito = 7

os.system("cls")

#mientras no el jugador no muera
while not end_game:
    #mientras el largo de la cantidad de objetos sea menor al numero de objetos se va a hacer esto
    #Si en el mapa recogemos un objeto el numero de obstaculos sera menor por eso se genera infinitamente, para hacerlo finito
    # es tan simple como hacer que solo se genere una vez
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

                    os.system("cls")
                    #Aqui se seleciona el pokemon rival aleatoriamente
                    poke_rival = random.randint(0, 6)
                    if poke_rival == 0:
                        poke_rival1 = pokemons[0]
                        poke_rival2 = pokemon0
                        poke_player2_damage = [14, 11]
                        hp_poke2 = 90
                        hp_poke2_total = hp_poke2
                    elif poke_rival == 1:
                        poke_rival1 = pokemons[1]
                        poke_rival2 = pokemon1
                        poke_player2_damage = [15, 11]
                        hp_poke2 = 95
                        hp_poke2_total = hp_poke2
                    elif poke_rival == 2:
                        poke_rival1 = pokemons[2]
                        poke_rival2 = pokemon2
                        poke_player2_damage = [14, 8]
                        hp_poke2 = 105
                        hp_poke2_total = hp_poke2
                    elif poke_rival == 3:
                        poke_rival1 = pokemons[3]
                        poke_rival2 = pokemon3
                        poke_player2_damage = [18, 9]
                        hp_poke2 = 90
                        hp_poke2_total = hp_poke2
                    elif poke_rival == 4:
                        poke_rival1 = pokemons[4]
                        poke_rival2 = pokemon4
                        poke_player2_damage = [6, 8]
                        hp_poke2 = 125
                        hp_poke2_total = hp_poke2
                    elif poke_rival == 5:
                        poke_rival1 = pokemons[5]
                        poke_rival2 = pokemon5
                        poke_player2_damage = [10, 8]
                        hp_poke2 = 125
                        hp_poke2_total = hp_poke2
                    elif poke_rival == 6:
                        poke_rival1 = pokemons[6]
                        poke_rival2 = pokemon6
                        poke_player2_damage = [-5, 8]
                        hp_poke2 = 140
                        hp_poke2_total = hp_poke2
                    else:
                        print("Opcion invalida")  # no se para que pero lo pongo xd
                    #combate pokemon
                    poke_attack_player = None
                    print("Combate Pokemon ",poke_player1,"VS",poke_rival1 )
                    print("\n \n" "El pokemon rival es {} y Sus ataques son {} y {}  \n".format(poke_rival1, poke_rival2[0],
                                                                                        poke_rival2[1]))
                    input("Pulse una tecla para continuar...")

                    os.system("cls")

                    while hp_poke > 0 and hp_poke2 > 0:
                        print("Turno de {}  \n".format(poke_rival1))
                        poke_attack_rival = random.randint(0, 1)
                        if poke_attack_rival == 0:
                            print("{} uso {} \n".format(poke_rival1, poke_rival2[0]))
                            hp_poke -= poke_player2_damage[0]
                        else:
                            print("{} uso {} \n".format(poke_rival1, poke_rival2[1]))
                            hp_poke -= poke_player2_damage[1]

                        print("La vida de tu pokemon ", poke_player1, "es" "[", "*" * int(hp_poke / 5),
                              " " * int((hp_poke_total - hp_poke) / 5), "]",
                              "[", hp_poke, "/", hp_poke_total)
                        print("La vida del pokemon rival", poke_rival1, "es" "," "[", "*" * int(hp_poke2 / 5),
                              " " * int((hp_poke2_total - hp_poke2) / 5), "]",
                              "[", hp_poke2, "/", hp_poke2_total, "\n")

                        print("Turno de {}  \n".format(poke_player1))

                        while poke_attack_player != "0" and poke_attack_player != "1":
                            poke_attack_player = input(
                                "Que ataque quieres usar (0){} o (1){} ".format(poke_player2[0], poke_player2[1]))
                        if poke_attack_player == "0":
                            print("{} uso {} \n".format(poke_player1, poke_player2[0]))
                            hp_poke2 -= poke_player1_damage[0]
                            poke_attack_player = None
                        elif poke_attack_player == "1":
                            print("{} uso {}\n".format(poke_player1, poke_player2[1]))
                            hp_poke2 -= poke_player1_damage[1]
                            poke_attack_player = None
                        else:
                            print("Respuesta incorrecta")

                        print("La vida de tu pokemon ", poke_player1, "es" "[", "*" * int(hp_poke / 5),
                              " " * int((hp_poke_total - hp_poke) / 5), "]",
                              "[", hp_poke, "/", hp_poke_total)
                        print("La vida del pokemon rival", poke_rival1, "es" "," "[", "*" * int(hp_poke2 / 5),
                              " " * int((hp_poke2_total - hp_poke2) / 5), "]",
                              "[", hp_poke2, "/", hp_poke2_total, "\n")
                        input("Pulse una tecla para continuar...")
                        os.system("cls")


                #objeto de vida
                if hp_in_cell:
                    map_hp.remove(hp_in_cell)
                    hp_poke += 30
                    if hp_poke > hp_poke_total:
                        hp_poke = hp_poke_total

                if tail_in_cell:
                    print("Has muerto")
                    end_game = True
                    died =  True
            if barrera[y][x] == "x":
                char_to_draw = "x"
            if hp_poke <= 0: #si la vida de tu pokemon es menor o igual a 0 significa que has muerto por lo cual termina el juego
                os.system("cls")
                print("\n Tu pokemon {} ha muerto ".format(poke_player1))
                print("\n Ha terminado el juego")
                input("\n Pulsa cualquier tecla...")
                end_game = True
                break

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (Map_Width ) + "+")

    print("Tamaño de la cola es {} ".format(tail_length))
    print("La vida de tu pokemon es {} ".format(hp_poke))
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


