import random

def generar_palabra():
    palabras = ["murciélago", "elefante", "computadora", "guitarra", "camarero", "bicicleta"]
    return random.choice(palabras)

def ocultar_letras(palabra):
    letras_mostradas = int(len(palabra) * 0.4)  # Ocultar al menos el 60% de las letras
    indices_mostrados = random.sample(range(len(palabra)), letras_mostradas)
    palabra_oculta = list(palabra)
    for i in range(len(palabra)):
        if i not in indices_mostrados:
            palabra_oculta[i] = '_'
    return ''.join(palabra_oculta)

def mostrar_palabra(palabra_oculta):
    print("Palabra a adivinar:", palabra_oculta)

def adivinar_palabra(palabra, palabra_oculta, intentos_restantes):
    while intentos_restantes > 0:
        print("\nIntentos restantes:", intentos_restantes)
        mostrar_palabra(palabra_oculta)
        intento = input("Introduce una letra o intenta adivinar la palabra completa: ").lower()
        if len(intento) == 1:
            if intento in palabra:
                print("¡Adivinaste una letra!")
                for i in range(len(palabra)):
                    if palabra[i] == intento:
                        palabra_oculta = palabra_oculta[:i] + intento + palabra_oculta[i+1:]
            else:
                print("La letra no está en la palabra.")
                intentos_restantes -= 1
        elif len(intento) == len(palabra):
            if intento == palabra:
                print("¡Felicidades! Adivinaste la palabra completa:", palabra)
                return
            else:
                print("La palabra no es correcta.")
                intentos_restantes -= 1
        else:
            print("Por favor, introduce una letra o una palabra de la misma longitud que la palabra a adivinar.")
    print("\n¡Lo siento! Te has quedado sin intentos. La palabra correcta era:", palabra)

def jugar():
    palabra = generar_palabra()
    palabra_oculta = ocultar_letras(palabra)
    intentos_restantes = 5  # Número de intentos permitidos
    print("¡Bienvenido al juego de adivinar palabras!")
    print("Tienes que adivinar una palabra en la que algunas letras están ocultas.")
    adivinar_palabra(palabra, palabra_oculta, intentos_restantes)

# Ejecutar el juego
jugar()
