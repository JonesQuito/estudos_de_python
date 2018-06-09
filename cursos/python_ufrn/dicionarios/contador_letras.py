letterCounts = {}
inventario = {'abacaxi': 430, 'banana': 312, 'laranja': 525, 'peras': 217}
for letra in inventario:
    letterCounts[letra] = letterCounts.get(letra, 0) + 1

print(letterCounts)