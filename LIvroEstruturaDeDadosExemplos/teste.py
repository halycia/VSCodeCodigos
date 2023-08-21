#PseudocodigoPrograma
#Declare num1, num2, resultado;
#Leia num1, num2;
num1, num2 = map(int, input().split(" "))
#Resultado = num1+num2;
#Escreva Resultado.
print(num1*num2)

#Mesmo pseudocodigo porém agora com função
#pra rodar direto no codigo
def Multiplicar(num1, num2):
    return num1*num2
print(Multiplicar(5,6))

def Multiplicar2():
    num1, num2 = map(int, input().split(" "))
    return num1*num2
print(Multiplicar2())

