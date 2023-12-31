#pesquisa binária
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
    #o meio é arredondado para baixo automaticamente
    #pelo Python se (baixo + alto) não for um número par
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
minha_lista = [1,2,3,4,5]
print(pesquisa_binaria(minha_lista,2))

#tempo de execução: log(n)
#porém, mandatory ser lista ordenada
