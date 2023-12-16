import os.path


def Question():
    question = "Que quieres hacer? (A)ñadir producto (G)uardar tu lista (V)er tu lista (S)alir (C)argar ultima lista"
    return question


def Add_product():
    Pregunta = None
    List_Add = []
    while Pregunta != "Nada":
        Pregunta = input("Que quieres añadir tenemos :Pan/Pollo/Pipas (Nada para salir)")
        if Pregunta in List_Add:
            print("Cabron")
        elif Pregunta == "Nada":
            break
        else:
            if Pregunta == "Pan":
                List_Add.append(Pregunta)
            elif Pregunta == "Pollo":
                List_Add.append(Pregunta)
            elif Pregunta == "Pipas":
                List_Add.append(Pregunta)
            else:
                print("Lo siento no hay de eso")
    return List_Add


def Save_list(Lista):
    Name = input("Como quieres que se llame el archivo")
    a = open( Name + ".txt", "w")
    a.write("\n".join((Lista)))
    a.close()
    print("Tu lista de la compra se ha guardado")


def Saw_list(My_List):
    print(My_List)


def Load_List():
    My_List = []
    while True:
        Name = input("Introduce el nombre del archivo que desea cargar")
        try:
            # if os.path.exists(Name + ".txt"):
            with open(Name + ".txt", "r") as a:
                print("{} esta cargado".format(Name))
                My_List = a.read().split("\n")
                break
        except FileNotFoundError:
            # else:
            print("Ese Archivo no existe ")
    return My_List

def Main ():
    My_List = []
    x = input(Question())
    while x != "S":
        if x == "G":
            Save_list(My_List)
        if x == "A":
            My_List = Add_product()
        if x == "V":
            Saw_list(My_List)
        if x == "C":
           My_List = Load_List()
        else:
           pass
        x = input(Question())
    return My_List


if __name__ == "__main__":
    Main()


