import random
import time
#------------------------------- Funciones ----------------------------------

def limpiarPantalla():
    print('\n' * 30)

def palabraEscogida():
    palabra = random.choice(['redes', 'ordenador', 'usuario', 'juego', 'programa',\
     'computacion', 'python', 'puertos', 'pantalla', 'variables', 'archivos','linux',\
     'software', 'git', 'macos', 'windows','microsoft', 'hash', 'internet', 'google', 'java', 'informacion',\
    'android', 'apple', 'tecnologia', 'hardware', 'actualizaciones' ])
    return palabra

def adivino(palabra, letrasIntentadas):
    for letra in palabra:
        if letra != '':
            if letra not in letrasIntentadas:
                return False
    return True

def mostrarTablero(palabra, letrasIntentadas, intentos, turno, letraIncorrecta):
    print('Turno: ', turno)
    print('Letras incorrectas: ', letraIncorrecta)
    print('Intentos restantes: ', INTENTOS_MAXIMOS-intentos)
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


def leerIntento(letrasIntentadas): #Revisa si la respuesta del jugador es una letra, y que no sea repetida
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
    respuesta = input('¿Desea volver a jugar? (s/n): ').lower()
    return respuesta == 's'
   

#----------------------- Principal -----------------------------------

INTENTOS_MAXIMOS = 7

print('Bienvenido(a) al juego del Ahorcado')
continuar = True

while continuar:
    palabra = palabraEscogida()
    letraIncorrecta = ''
    letrasIntentadas = ""
    intentos = 0
    turno = 1
    while intentos < INTENTOS_MAXIMOS and not adivino(palabra, letrasIntentadas):
        mostrarTablero(palabra, letrasIntentadas, intentos, turno, letraIncorrecta)
        letra = leerIntento(letrasIntentadas)
        if aciertaIntento(palabra, letra):
            print('Has adivinado :D')
        else:
            print('Has fallado :(')
            letraIncorrecta = letraIncorrecta + letra + ' '
            intentos = intentos + 1
        letrasIntentadas = letrasIntentadas + letra + ' '
        turno = turno + 1
        time.sleep(1)
        limpiarPantalla()
    if adivino(palabra, letrasIntentadas):
        print('¡Felicidades! Adivinaste la palabra: ', palabra)
    else:
        print('Has perdido :(. La palabra era: ', palabra)
    continuar = otraVez()
print('\nMuchas gracias por jugar :D\n¡Tenga un lindo día!')
