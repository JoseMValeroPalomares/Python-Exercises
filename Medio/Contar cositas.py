texto= input("Di tu textamento")
espacio = " "
nespacio = int(0)
puntos = "."
npuntos = int(0)
comas = ","
ncomas= int(0)


for letras in texto:
    if letras == espacio in texto:
        nespacio += 1
for letras in texto:
    if letras == puntos in texto:
        npuntos += 1
for letras in texto:
    if letras ==comas in texto:
        ncomas += 1
print("Los espacios son {} , Los puntos son {}, Las comas son {}".format(nespacio,npuntos,ncomas))