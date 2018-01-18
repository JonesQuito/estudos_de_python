from recomendacao import avaliacoes

def printtAll():
    for usuario in avaliacoes:
        print(usuario)
        for filme in avaliacoes[usuario]:
            print("\t",filme)
        print()


printtAll()