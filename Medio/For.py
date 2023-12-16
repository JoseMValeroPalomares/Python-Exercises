vocales = ["a", "e", "i", "o", "u",]

frase = "Maricon quien lo lea (Sip tengo 16 años y todavia digo cosas de estas pasa algo?"

vocales_xd = 0
for x in frase:
    if x in vocales:
        print("He encontrado una {}".format(x))
        vocales_xd += 1

print("Hay {} vocales".format(vocales_xd))

n= int(input("Di el numero de repes"))
for a in range(n):
    print("a")