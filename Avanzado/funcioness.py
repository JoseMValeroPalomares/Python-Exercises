def fibonarri(x):
   list = []
   a = 1
   for i in range (x):
       print(a)
       list.append(a)
       a = a + list[i-1]


def potencia (x,y):

    x -= +1
    y2= y
    for i in range (x):
        y2= y2*y
    print("La potencia  de {} a la {} es {}".format(y,x+1,y2))


if __name__ == "__main__":
    y = int(input("Di el numero del que desea sabe su potencia"))
    x = int(input("Di a cuanto esta elevado"))
    potencia(x,y)