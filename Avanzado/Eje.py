import random
import string


def String_larga(x):
    strings = []
    more_lenn = 0
    for i in range (x):
        add_string = input("Dime la {} string".format(i+1))
        largo = len(add_string)
        if largo > more_lenn:
            more_lenn = largo
            more_len = i
        strings.append(add_string)

    print(strings)
    print("La string mas larga es la {} ".format(strings[more_len]))

def Suma_lista(x):
    nums = []
    suma = 0
    for i in range (x):
        add_num = int(input("Di el {} numero que vas a sumar".format(i+1)))
        suma += add_num
        nums.append(add_num)
    print("La suma de todos esos numeros es {}".format(suma))

def Is_Impar(x):
    Impar = x % 2
    if Impar == 0 :
        print("{} No es impar".format(x))
    else:
        print("{} Si es impar".format(x))

def Are_you_sure():
    x = None
    Question = None
    while Question !="S" and Question !="N":
        Question = input("Estas seguro? S/N")
    if Question == "S":
        x = True
    elif Question == "N":
        x=False
    return x

def String_Mayus():
    mayus_alphabet = 'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z'
    minus_alphabet = 'a b c d e f g h i j k l m n ñ o p q r s t u v w x y z'

    ABC = mayus_alphabet.split()
    abc = minus_alphabet.split()

    sentence = input('Escribe la frase: \n')
    sentence_list = list(sentence)

    for l in range(len(sentence_list)):
        if sentence_list[l] in abc:
            for m in range(len(abc)):
                if sentence_list[l] == abc[m]:
                    sentence_list[l] = ABC[m]
                    sentence = "".join(sentence_list)
    print(sentence)

def Num_Random():
    x = random.randint(0,100)
    return x
def Guess_Number():
    User_Number = True
    while User_Number == True:
            Answer = int(input("Di un numero"))
            if Answer == Num_Random():
                print("Los has adivinado")
            else:
                print("Try again")



def Add_Item_List():
    x = input("Que desea añadir?")
    List_Shop2 = [x]
    List_Shop2.append(x)
    return List_Shop2





def main():
    List_Shop = ["Pan","Agua","Carne","Pescado"]
    Answer = input("Quieres añadir algo? S/N")
    if Answer =="S":
        x = Add_Item_List()
        if x[0] in List_Shop:
            print("Ya hay de eso")
        else:
            List_Shop.append(x[0])
    else:
        pass
    print("Tu lista es {}".format(List_Shop))





if __name__ == "__main__":
    main()