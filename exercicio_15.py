"""exercicio 15
autor: vinicius
instrução: leia do teclado 3 valores reais e os imprima na tela em ordem crescente
versão: 0.0.1"""


# Alocação de memoria

valor1 = ""
valor2 = ""
valor3 = ""


## Entrada de dados

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

# Processamento de dados

valores = [valor1, valor2, valor3]
valores.sort()

#Saída de dados
print(valores)