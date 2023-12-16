import random
import os
hp_pikachu=80
hp_squirtle=90
hp_pikachu_total = 80
hp_squirtle_total = 90

while hp_pikachu > 0 and hp_squirtle > 0:

    print("Turno de pikachu")
    ataque_pikachu = random.randint(1,2)
    if ataque_pikachu == 1:
         print("Pikachu uso bola voltio")
         hp_squirtle -= 9
    elif ataque_pikachu == 2:
        print("Pikachu uso onda trueno ")
        hp_squirtle -= 10
    print("La vida de Pikachu es", "[", "*" * int(hp_pikachu / 5)," " * int((hp_pikachu_total - hp_pikachu) /5), "]", "[",hp_pikachu,"/", hp_pikachu_total, "]")
    print("La vida de Squirtle es", "[", "*" * int(hp_squirtle / 5)," " * int((hp_squirtle_total - hp_squirtle) /5), "]", "[",hp_squirtle,"/", hp_squirtle_total,"]")
    input("Pulse cualquier tecla para continuar \n")
    print("Turno de squirtle")

    ataque_squirtle= None
    while ataque_squirtle != "P" and ataque_squirtle != "p" and  ataque_squirtle != "B" and ataque_squirtle != "b" and  ataque_squirtle !="A" and ataque_squirtle !="a":
        ataque_squirtle=input("Que ataque quieres realizar (P) Placaje (A) Pistola agua (B) Burbujas")
    if ataque_squirtle == "P" or "p":
        print("Squirtle uso  Placaje")
        hp_pikachu -= 6
    elif ataque_squirtle == "B" or "b":
        print("Squirtle uso Burbujas")
        hp_pikachu -= 90
    elif ataque_squirtle == "A" or "a":
        print("Squirtle uso Pistola agua")
        hp_pikachu -= 15
    print("La vida de Pikachu es", "[", "*" * int(hp_pikachu / 5)," " * int((hp_pikachu_total - hp_pikachu) /5), "]","[",hp_pikachu,"/", hp_pikachu_total, "]")
    print("La vida de Squirtle es", "[", "*" * int(hp_squirtle / 5)," " * int((hp_squirtle_total - hp_squirtle) /5), "]", "[",hp_squirtle,"/", hp_squirtle_total, "]")
    input("Pulse cualquier tecla para continuar \n")
    os.system ("cls")
if hp_pikachu > hp_squirtle:
    print("Pikachu gano el combate \n")
else:
    print("Squirtle gano el combate \n")



