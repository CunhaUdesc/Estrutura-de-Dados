import sys

## Repetição com for


# range() define a quantidade de vezes que será executado
for i in range(0, 11,1 ):
    print('teste')

s = [1,2,3]
for i in s:
    print('teste')
# len(s) retorna o tamanho (equivalente ao length

# Definição de funções
def perfeito(numero):
    print('Código identado')
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
    return soma == numero

# Pegar todos os números informado no console
numeros = sys.argv[1:-2] # Todos menos os dois últimos
x, y = int(sys.argv[-2]), int(sys.argv[-1])