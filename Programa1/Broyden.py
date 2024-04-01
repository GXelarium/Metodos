import numpy as np # Para hacer cálculos con vectores
import funciones as f # script con las funciones 


def newton(vector,op):
    """
    Método de Newton para calcular el segundo punto

    Args:
    vector: Punto inicial
    op: Opción del sistema a solucionar

    Return:
    Vector resultante
    """
    # Se guarda los valores de la función y la jacobiana
    funcion = f.func(vector,op)
    jacobiana = f.jacob(vector,op)

    # Se calcula el siguiente punto
    prod = np.matmul(np.linalg.inv(jacobiana),funcion)
    resultado = vector-prod

    return resultado

def Jacobinv(a,vector1, vector2,op):
    """
    Cálculo de la Jacobiana inversa utilizando 
    el teorema de Sherman-Morrison

    Args:
    a: Valor obtenido anteriormente
    vector1: Punto actual
    vector2: Punto anterior
    op: Opción del sistema a solucionar

    Return:
    Matriz de la jacobiana inversa.
    """
    # Incrementos de los puntos y las funciones
    dX = vector1-vector2
    dF = f.func(vector1,op) - f.func(vector2,op)

    # Aplicación del teorema de Sherman-Morrison
    numerador = np.matmul(dX - np.matmul(a,dF),np.matmul(np.transpose(dX),a))
    denominador = np.matmul(np.matmul(np.transpose(dX),a),dF) 
    resultado = a + (1/denominador) * numerador

    return resultado

def imprimir(i,p1,p2,J,op):
    print("{}".format(i), end=" ")
    for i in range(len(p1)):
        print("\t\t{:.6f}\t {:.6f}".format(p1[i],f.func(p1,op)[i]),end=" ")
        for j in range(len(p1)):
            print("\t\t{:.6}".format(J[i][j]),end=" ")
        print("\t\t{:.6f}\t {:.6f}".format(p2[i],f.func(p2,op)[i]),end=" ")
        print("")
    error = np.absolute(f.func(p2,op)).max()
    print("Error: \t{:.6f}".format(error))
    print("")
    return error

# Aquí solo es una idea
def Broyden(F,op,tol=0.0005,max=10):
    """
    Solución del sistema de ecuaciones por el método de Broyden

    Args:
    F: Punto inicial
    op: Opción del sistema a solucionar
    tol: Toleranacia
    max: Número máximo de iteraciones

    """
    # Columnas de las tablas
    print("")
    if len(F)==3:
        print("Iteración \tPunto(k-1) \t Función(K-1) \t\t\tJacobiana inversa \t\t Punto(k) \tFunción(k)")
    else:
        print("Iteración \tPunto(k-1) \t Función(K-1) \t\t\tJacobiana inversa \t\t\t Punto(k) \tFunción(k)")
    print("")

    pa = F
    vector = newton(F,op)
    j = np.linalg.inv(f.jacob(F,op))
    error = imprimir(1,pa,vector,j,op)
    for i in range(1,max):
        jinv = Jacobinv(j,vector,pa,op)
        pa = vector
        vector = vector - np.matmul(jinv,f.func(vector,op))
        error = imprimir(i+1,pa,vector,jinv,op)
        j = jinv
        if error < tol:
            break
        iteraciones = i+1
    print("Iteraciones:{}\nError:{:.6}".format(iteraciones,error))



print(Broyden([2,1],1,0.0005,15))




