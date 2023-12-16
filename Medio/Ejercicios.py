
#numeros2 = (input("Di numeros con una coma"))
#numeros = numeros2.split(",")
#print(numeros)


numeros2 = (input("Di numeros con una coma"))
numeros =[int(x) for x in numeros2.split(",")]
print(numeros)

numero_peque = numeros[0]
numero_grande = numeros[0]

for x in numeros:
    if numero_peque < x :
        numero_peque = x
    if numero_grande > x:
        numero_grande = x

print(numero_peque,numero_grande)


