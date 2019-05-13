entradas = [1,7,5]
pesos = [0.8,0.1,0]

def soma (entrada, peso):
    soma = 0
    for i in range(3):
        soma += entrada[i] * peso[i]
    return soma

rSoma = soma(entradas, pesos)

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

result = stepFunction(rSoma)