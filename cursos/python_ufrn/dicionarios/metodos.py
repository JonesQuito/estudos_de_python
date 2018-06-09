"""
    Os métodos são semelhantes às funções, porém a sintaxe é diferente.
    Para usarmos funções, chamamos o nome da função e passamos os argumentos
    para seus parâmetros, se houver.
    No caso dos métodos, os mesmos são precedidos pelo objeto que o contém
    Ex: nome_objeto.nome_metodo()
"""
ing2esp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
inventario = {'abacaxi': 430, 'banana': 312, 'laranja': 525, 'peras': 217}
print(inventario.keys())                # O método keys() retorna todas as chaves de um dicionário
print(inventario.values())              # O método values() retorna todos os valores de um dicionário
print(inventario.items())               # O método items() retorna todos os itens de um dicionário
print(ing2esp.__contains__('one'))      # O método __contains__('chave') retorna True se a chave existe no dicionário