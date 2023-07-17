#PseudocodigoPrograma
#Declare num1, num2;
#Leia num1, num2 em uma entrada só, com os fatores separados por espaço;
num1, num2 = map(int, input().split(" "))
print(num1*num2)
#ou atribuir resultado a variável;
resultado = num1*num2

#Mesmo pseudocodigo porém agora com função
def Multiplicar(num1, num2):
    return num1*num2
print(Multiplicar(5,6))

def MultiplicarComInput():
    num1, num2 = map(int, input().split(" "))
    return num1*num2
print(MultiplicarComInput())