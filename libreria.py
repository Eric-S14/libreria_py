#Actividad 2
from mi_paquete.redondeo import redondear

def suma_redondeada(a, b):
    suma = a + b
    return redondear(suma)


resultado = suma_redondeada(1.2, 2.3)
print(resultado)

resultado = suma_redondeada(1.6, 2.1) 
print(resultado)
#Actividad 1
'''actividad 1
def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)

print(redondear(3.49))
print(redondear(3.50))
print(redondear(3.51))
print(redondear(4.99))
'''
#Actividad 3
'''import datetime

fecha_hora_actual = datetime.datetime.now()

print("Fecha y hora actuales:", fecha_hora_actual)
'''
#Actividad 4
'''import random

numero_par = random.choice([2, 4, 6, 8, 10])

print("Número par al azar:", numero_par)
'''
#Actividad 5
'''import random

def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]

    respuesta_aleatoria = random.choice(respuestas)
    
    return respuesta_aleatoria

print("Pregunta a la bola mágica:")
input("Haz tu pregunta: ")
print("La bola mágica dice:", bola_magica())'''

#Actividad 6

# bola magica

#import random
#import time

#def bola_magica(pregunta):
#    respuestas = [
#        "Es seguro que sí",
#        "Las chances son buenas",
#        "Puedes contar con ello",
#        "Preg'''úntame de nuevo más tarde",
#        "Concéntrate y pregunta de nuevo",
#        "No veo con claridad, intenta de nuevo",
#        "Mi respuesta es no",
#        "Mis fuentes me dicen que no"
#    ]
#    return random.choice(respuestas)

#start_time = time.time()

#for _ in range(1000000):
#    bola_magica("¿Debería estudiar más?")

#end_time = time.time()

#execution_time = end_time - start_time
#print(f"Tiempo de ejecución de la función bola_magica: {execution_time} segundos")

# el primer actividad
'''import time

def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)

start_time = time.time()

print(redondear(3.49))
print(redondear(3.51))

end_time = time.time()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time} segundos")
'''
''' actividad 2 sin el paquete
def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)

def suma_redondeada(a, b):
    resultado = a + b
    return redondear(resultado)

numero1 = 2.45
numero2 = 1.10
print(f"La suma redondeada de {numero1} y {numero2} es: {suma_redondeada(numero1, numero2)}")
'''
