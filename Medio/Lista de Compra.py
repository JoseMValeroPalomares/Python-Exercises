lista = []
x=None
print("Bienvenido al SuperMercado")
while x != "Q" and x != "q":
    x=input("Que desea comprar? (Q para salir) ")
    if x == "q" or x == "Q":
        print("Adios ;c")
    else:
        if x not in lista:
            pregunta=input("Seguro que quieres comprar {} (Si/No)".format(x))
            if pregunta == "Si" or pregunta == "si" or pregunta == "s" :
                lista.append(x)
                print("{} esta en tu lista de compra".format(x))
            else:
                print("Tus muertos")
        else:
            print("Eso esta en la lista ya hijo de puta")


print("\n Tu lista es ",lista)