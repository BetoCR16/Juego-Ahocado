import random
import time
#------------------------------- Funciones ----------------------------------

def limpiarPantalla():
    print('\n' * 20)

def palabraEscogida():
    palabra = random.choice(['redes', 'ordenador', 'persona', 'juego', 'programa', 'computacion', 'python', 'puertos', 'pantalla', 'variables', 'inteligencia', ])
    return palabra

def adivino(palabra, letrasIntentadas):
    for letra in palabra:
        if letra != '':
            if letra not in letrasIntentadas:
                return False
    return True

def mostrarTablero(palabra, letrasIntentadas, intentos, turno):
    print('Turno: ', turno)
    print('Letras utilizadas: ', letrasIntentadas)
    print('Intentos: ', intentos)
    print()
    print(textoOculto(palabra, letrasIntentadas))
    print()

def textoOculto(palabra, letrasIntentadas):
    resultado = ''
    for letra in palabra:
        if letra in letrasIntentadas:
            resultado += letra + ' '
        else:
            resultado += "_ "
    return resultado

def leerIntento(letrasIntentadas):
    print()
    letra = input('Escriba una letra: ').lower()
    while len(letra) != 1 or letra not in 'abcdefghijklmnñopqrstuvwxyz' or letra in letrasIntentadas:
        print('Escribe otra letra. Letras utilizadas: ', letrasIntentadas)
        letra = input('Escriba una letra: ').lower()
    print()
    return letra

def aciertaIntento(palabra, letra):
    return letra in palabra

def otraVez():
    print()
    respuesta = input('Desea volver a jugar? (s/n): ').lower()
    return respuesta == 's'
   

#----------------------- Principal -----------------------------------

INTENTOS_MAX = 7

print('Bienvenido(a) al juego del Ahorcado')
continuar = True

while continuar:
    palabra = palabraEscogida()
    letrasIntentadas = ""
    intentos = 0
    turno = 1
    while intentos < INTENTOS_MAX and not adivino(palabra, letrasIntentadas):
        mostrarTablero(palabra, letrasIntentadas, intentos, turno)
        letra = leerIntento(letrasIntentadas)
        if aciertaIntento(palabra, letra):
            print('Has adivinado :D')
        else:
            print('Has fallado :(')
            intentos = intentos + 1
        letrasIntentadas = letrasIntentadas + letra
        turno = turno + 1
        time.sleep(1)
        limpiarPantalla()
    if adivino(palabra, letrasIntentadas):
        print('Felicidades! Adivinaste la palabra: ', palabra)
    else:
        print('Has perdido :(. La palabra era: ', palabra)
    continuar = otraVez()
print('Muchas gracias por jugar :D')