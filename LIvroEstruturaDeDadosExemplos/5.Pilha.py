def regressiva(i):
    if i <= 1:
        return 
    regressiva(i-1)


'''inicial = int(input())
i = inicial
while i >= 0:
    print(i)
    i -=1
'''

#dois códigos diferentes: o primeiro não printa,
#mas usa call stack (recursão)
#o segundo printa, mas não usa recursão nem função :(

#o pc usa pilha de chamada

def sauda(nome):
    print("Olá. " + nome + " !")
    sauda2(nome)
    print("Preparando para dizer tchau...")
    tchau()

def sauda2(algo):
    x = str(len(algo))
    print(f"Seu nome tem {x} letras!")
    
def tchau():
    print("Ok, byee")
    
#caso sua pilha use memória demais, você pode usar
#uma tail recursion (recursão de cauda) ou reescrever
#o código usando loop
    