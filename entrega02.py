import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def readFile():
    fname = input("Al ingresar el nombre del archivo recuerde que debe ingresar su tipo. Ej: input.txt \nTambien recuerde que el archivo .txt debe estar en la misma carpeta que este archivo .py\nIngrese el nombre del archivo: ")
    if len(fname) < 1 : fname = "input.txt"
    f = open(fname)
    text = ""
    for line in f.read().strip().split("\n"):
        text += line
    return text


def updateDictionaries(probs: dict):
    for key in probs.keys():
        probs.update({key: createProb(probs.get(key))})


def createProb(letters: list) -> dict:
    freq = {}
    for letter in letters:
        freq[letter] = letters.count(letter)/len(letters)
    return freq


def createText(length: int, text: str, probs:dict)->None:
    j = 0
    l = len(text)
    while len(text)!=length:
        if probs.get(text[j:j+l], -1) == -1:
            print("No se pudo seguir generando más texto")
            break
        keys = [key for key in probs[text[j:j+l]].keys()]
        text += np.random.choice(keys, p=[probs[text[j:j+l]].get(key) for key in keys])
        j+=1
    print("El texto generado es: "+text)


def showHistogram(probs: dict) -> None:
    keys = probs.keys()
    if len(keys) > 1:
        cadenas = [key for key in keys]
        values = [len(probs.get(cadena)) for cadena in cadenas]
    else:
        keys = probs['']
        cadenas = []
        [cadenas.append(cadena) for cadena in keys if cadena not in cadenas]
        values = [keys.count(cadena) for cadena in cadenas]

    x = np.arange(len(cadenas))
    width = 0.35

    fig, ax = plt.subplots()
    rects = ax.bar(x, values, width, color = 'red')
    
    ax.set_ylabel('Frecuencia')
    ax.set_title('Diagrama de frecuencias de las K-tuplas')
    ax.set_xticks(x)
    ax.set_xticklabels(cadenas)

    ax.bar_label(rects, padding=2)
    fig.tight_layout()
    plt.show()


def main():
    print()
    text = readFile()
    k = int(input("Ingrese K "))
    probs = dict()
    

    for i in range(len(text)-k):
        probs[text[i:i+k]] =  probs.get(text[i:i+k], []) + [text[i+k]]

    hist = probs.copy()
    updateDictionaries(probs)
    ejecutando = True

    while ejecutando:
        print("Menu de opciones")
        print(" 1 - Hacer texto de longitud N")
        print(" 2 - Mostrar Histograma")
        print(" 3 - Salir de la aplicación")

        opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
        
        if opcion_elegida == "1":
            print()
            createText(int(input("Ingrese el valor de N: ")), text[0:k], probs)
        elif opcion_elegida == "2":
            showHistogram(hist)
        elif opcion_elegida == "3":
            ejecutando = False
        else:
            print("La opcion " + opcion_elegida + " no es una opción valida.")
        print()


if __name__ == "__main__":
    main()

