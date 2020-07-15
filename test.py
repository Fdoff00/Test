from random import randint
print("Jugaremos al ahorcado.")
palabras = ["hola", "foca", "loco", "pans", "teni"]
win = False
intento = 0
acierto = 0
n = randint(0,(len(palabras)-1))
print(n)
correctas = []
print(len(palabras[n]))
if(intento == 0):
    for i in range(len(palabras[n])):
        correctas.append("_ ")
while(win == False):
    for i in range(len(correctas)):
        print(correctas[i],end="")
    print()
    intento = input("Ingrese la letra: ")
    if(intento != palabras[n]):
        if(intento in palabras[n]):
            for i in range(len(correctas)):
                if(intento == palabras[n][i]):
                    correctas[i] = intento
                    acierto += 1
                    if(acierto == len(correctas)):
                        win = True
            print(intento)
        else:
            print("---Incorrecto---")
    else:
        win = True
print("\n\nGANASTE EL JUEGO.\nLa respuesta es: ")
print(palabras[n])
