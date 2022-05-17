import random


# ----  Ejercicios ---- 

#Ejercicio 1
def pintaMenu():
    print("1-Guardar asignatura")
    print("2-Borrar asignatura")
    print("3-Ver nota media")
    print("4-Ver todas las asignaturas")
    print("5-Salir")
    opcion = 0
    while opcion<1 or opcion>5:
        bandera = True
        while (bandera == True):
            try:
                opcion =(int)(input("Seleccione la opción que desees: "))
                bandera = False
            except:
                print("Te has equivocado")
        
    return opcion
#Fin ejercicio 1

#Ejercicio 3
def opcion1(asignaturas):
    asignaturasAle=input("Selecciona una asignatura: ")
    asignaturas.append(asignaturasAle)
    return asignaturas
#Fin ejercicio 3

#Ejercicio 4
def eliminarAsig(asignaturas):
    eliminar =input("¿Qué asignatura quieres borrar? ")
    try:
        asignaturas.remove(eliminar)
        return True
    except:
        return False

#Fin ejercicio 4

#Ejercicio 5
def numAleatorio(numero):
    lista = []
    i = 0
    while i<numero:
        lista.append(random.randint(0,10))
        i = i + 1
    return lista
#Fin ejercicio 5

#Ejercicio 6
def notaMedia():
    notas=numAleatorio()
    media = 0
    suma = 0
    for i in notas:
        suma = suma + i
    media = suma/notas

#Fin ejercicio 6

#Ejercico 7

#Fin ejercicio 7

# ---- Programa principal -----

#Ejercicio 2
asignaturas = []
opcion = pintaMenu()
while opcion != 5:
    if (opcion==1):
        asignaturas = opcion1(asignaturas)
        print(asignaturas)
    if (opcion==2):
        asignaturas = eliminarAsig(asignaturas)
        print(asignaturas)
    if (opcion==3):
        print("Elige otra opción")
    if (opcion==4):
        print("Elige otra opción")
    else:
        break

    opcion = pintaMenu()






