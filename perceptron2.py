import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])


def soma (entrada, peso):
    return entrada.dot(peso)


def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0



rSoma = soma(entradas, pesos)
result = stepFunction(rSoma)