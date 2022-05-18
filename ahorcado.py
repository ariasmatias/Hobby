word=input("ingrese una palabra para jugar al ahorcado: ").upper()
n= len(word)
intentos =len(word)
aciertos=["_"]*n

while intentos > 0:

    ganado=False
    encontrado=False

    letra=input("Ingrese una letra: ").upper()

    for i in range (0,n):
        if letra == word[i]:
            aciertos[i]=letra
            encontrado=True

    if not encontrado:
            intentos=intentos -1
            print (f"Le quedan {intentos} intentos")

    if "".join(aciertos)==word:
        ganado=True
        intentos=0

if ganado == True:
    print("Ganaste")
else:
    print("Perdiste")