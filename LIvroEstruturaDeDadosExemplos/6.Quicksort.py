# divide to conquer
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total
#print(soma([1,2,3,4]))

def soma_usando_recursao(lista):
    if lista == []:
        return 0
    return lista[0]+soma_usando_recursao(lista[1:])
#print(soma_usando_recursao([1,2,3]))

#escreva uma função recursiva que conte o número
#de itens em uma lista
def contador_de_itens(lista):
    if lista == []:
        return 0
    return 1+ contador_de_itens(lista[1:])
print(contador_de_itens([1,2,3,4]))

# encontre o valor mais alto em uma lista
#cinco linhas
def encontra_maior_valor(lista):
    if lista == []:
        return None
    return 