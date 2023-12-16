titulo = "Bienvenido al test uwu"
print("\n"+ titulo + "\n" + "_" * len(titulo)+"\n")

puntuacion = 0

opcion = input("Pregunta 1: Que haces cuando alguien escribe uwu \n"
               "A  -Me lo intento fornicar \n"
               "B  -Lo intento matar \n"
               "C  -Hago la a y la b junto a la c haciendo un bucle infinito ")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 9999
else:
    exit()


opcion = input("""Pregunta 2: Que haces cuando alguien escribe uwu?? 
               A  -Me lo intento fornicar 
               B  -Lo intento matar 
               C  -Hago la a y la b junto a la c haciendo un bucle infinito""")




if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 9999


print(puntuacion)
