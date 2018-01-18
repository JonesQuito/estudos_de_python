from math import sqrt
from recomendacao import avaliacoes
#import functions


def euclidiana(usuario1, usuario2):
    si = {}
    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]: si[item] = 1
    if len(si) == 0: return 0
    soma = sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)
                  for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]])
    return 1 / (1 + sqrt(soma))



# elclidiana2
def euclidiana2(usuario1, usuario2):
    si = {}
    soma = 0
    for item in avaliacoes[usuario1]:
        if avaliacoes[usuario2].__contains__(item): si[item] = avaliacoes[usuario1][item]
    if len(si) == 0: return 0
    for item_comum in si:
        soma = soma + pow(si[item_comum] - avaliacoes[usuario2][item_comum], 2)
    return 1 / (1 + sqrt(soma))



# elclidiana3
def euclidiana3(usuario1, usuario2):
    si = {}
    soma = 0
    for item in avaliacoes[usuario1]:
        if avaliacoes[usuario2].__contains__(item):
            soma = soma + pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)
    return 1 / (1 + sqrt(soma))



def verificarTodas(usuario):
    for item in avaliacoes:
        if item != usuario:
            print("Similaridade de", str(usuario).upper(),"X", str(item).upper(), euclidiana(usuario, item))


verificarTodas('Ana')

"""
print(euclidiana2('Ana', 'Marcos'))
print(euclidiana('Ana', 'Pedro'))
print(euclidiana2('Ana', 'Claudia'))
print(euclidiana3('Ana', 'Adriano'))
print(euclidiana3('Ana', 'Janaina'))
print(euclidiana3('Ana', 'Leonardo'))
print(euclidiana3('Ana', 'Ana'))

"""

