import numpy as np

taxaAprendizagem = 0.1


#and
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0, 0, 0, 1])

#or
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0, 1, 1, 1])

#xor
entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0, 1, 1, 0])

pesos = np.array([0.0, 0.0])


def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    soma = registro.dot(pesos)
    return stepFunction(soma)

def treinar():
    erros = 1
    while (erros != 0):
        erros = 0
        for i in range(len(saidas)):
            calculoSaida = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - calculoSaida)
            erros += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado ' + str(pesos[j]))

treinar()
    