"""exercicio 6
autor: vinicius
instruçao: determine o n-esimo termo e a soma dos termos de uma progressao aritmetica onde n,
primeiro termo e a razao sao dados pelo usuario
versao: 0.0.1"""

# Alocação de memoria

a1 = None
razao = None
n_termos = None

# Entrada de dados

a1 = int(input("digite um numero: "))
razao = int(input("digite uma razao: "))
n_termos = int(input("digite o numero de termos: "))

# Processamento de dados

an = a1 + (n_termos - 1) * razao
soma = (n_termos * (a1 + an)) // 2 

#Saída de dados

print(an)
print(soma)