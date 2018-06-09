"""
    Nos exemplos abaixo, se uma alteração for feita em alias ou em oposites,
    elas serão refletidas em ambos os objetos, pois a operação alias = oposites
    faz com que os dois nomes/referências apontem para o mesmo objeto em memória,
    logo, as alterações em um irão refletir no outro

    Quando desejamos obter uma cópia idependente do objeto original, devemos usar o método .copy().
    Esse método cria uma nova instância de objeto que terá valores idênticos aos originais mas, em
    pontos diferentes da memória
"""

oposites = {'up':'dow', 'rignt': 'wrong', 'true':'false'}
print(oposites)

alias = oposites
print(alias)

copy = oposites.copy()
print(copy)

alias['true'] = 'False'
oposites['up'] = 'DOW'
copy['bonito'] = 'feio'
print("Alias", alias)
print("Oposites", oposites)
print("Copy:", copy)