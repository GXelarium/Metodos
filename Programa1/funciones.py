import numpy as np

def func(F,op):
    x = F[0]
    y = F[1]

    if op==1:
        return np.array([x**2 + x*y - 10,
                        y + 3*x*y**2 - 20])
    

    elif op==4:
        z = F[2]

        return np.array([x**2 - 4*x + y**2,
                        x**2 - x - 12*y + 1,
                        3*x**2 - 10*x + y**2 - 3*z**2 + 6])

def jacob(F,op):
    x = F[0]
    y = F[1]

    if op == 1:
        return np.array([[2*x + y, x],
                        [3*y**2, 6*x*y + 1]])
    

    elif op==4:
        z = F[2]

        return np.array([[2*x - 4, 2*y, 0],
                            [2*x - 1, -12, 0],
                            [6*x - 10, 2*y, -6*z]])