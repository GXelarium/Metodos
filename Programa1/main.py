import Broyden
import numpy as np
import os

def limpiar():
        if os.name == "posix":
                os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system ("cls")

def metodo(opcion):
        X = list(map(float, input("Introduce el punto inicial separado por espacios: ").split(' ')))
        max = int(input("Introduce el máximo de iteraciones: "))
        tol = float(input("Introduce la tolerancia: "))
        Broyden.Broyden(X,max,tol,opcion)
    


def menu():
    print(""" PROGRAMA 1: MÉTODO DE BROYDEN

Elaborado por:
-López Medina Andrés Alejandro



        
        Elige un sistema de ecuaciones:

        1)   
                f1(x,y) = x² + xy - 10 = 0
                f2(x,y) = y + 3xy² - 20 = 0
        

        4) 
                f1(x,y,z) = x² - 4x + y**2 = 0
                f2(x,y,z) = x² - x - 12y + 1 = 0
                f3(x,y,z) = 3x² - 10x + y² - 3z² + 6 = 0

       """)

    opcion = int(input("Sistema de ecuaciones número: "))
    if opcion > 0 and opcion < 5:
        loop = True
        while loop:
                metodo(opcion)
                estado = input("¿Quieres introducir otros valores? S/N: ").lower()
                if estado != 's':
                     loop = False
    else:
        print("Escoge un sistema válido")

    
    




if __name__ == '__main__':
    loop = True
    while loop:
        limpiar()
        menu()
        estado = input("¿Quieres resolver otro sistema? S/N: ").lower()
        if estado != 's':
             loop = False