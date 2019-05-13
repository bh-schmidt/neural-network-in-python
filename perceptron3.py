import numpy as np

taxaAprendizagem = 0.1

entradas = np.array([
            [0,0], [0,1], [1,0], [0,0]
        ])

saidas = np.array([
            0, 0, 0, 1
        ])

pesos = np.array([
            0.0, 0.0
        ])

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    soma = registro.dot(pesos)
    return stepFunction(soma)

def treinar():
    return 0
    