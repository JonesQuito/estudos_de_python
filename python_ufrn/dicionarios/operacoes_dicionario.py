# o comando 'del' remove um par chave-valor do dicionario
inventario = {'abacaxi': 430, 'banana': 312, 'laranja': 525, 'peras': 217}
print(inventario)


# excluíndo o elemento peras do inventario
del inventario['peras']
print(inventario)


# reinserindo o elemento 'peras' no inventário
inventario['peras'] = 154
print(inventario)



# Alterando a quantidade de peras para zero
inventario['peras'] = 0
print(inventario)

# Adicionando uvas no inventário
inventario['uvas'] = 52
print(inventario)

# Para obtermos o número de pares chave-valor usamos a função len(nome_dicionario)
tamanho_inventario = len(inventario)
print('Tamanho do inventário:', tamanho_inventario)