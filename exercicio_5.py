"""exercicio 4
autor: vinicius
instruçao: calcule o salario de um professor horista na Universidade XYZ. O programa deve perguntar o n´umero de horas trabalhadas, calcular e imprimir na tela o valor do sa´ario bruto,
do salario lıquido e do total de descontos, sabendo que o desconto do imposto é 30% e
que o valor da hora-aula é R$ 40,00
versao: 0.0.1"""

# Alocação de memoria

horas_trabalhadas = ""

# Entrada de dados

horas_trabalhadas = int(input("escreva o numero de horas trabalhadas: "))

# Processamento de dados
salario_bruto = 40*horas_trabalhadas
desconto = salario_bruto*0.3
salario_liquido = salario_bruto - desconto

#Saída de dados

print("\n" + "salario bruto:" + str(salario_bruto) + "\n",
     "desconto:" + str(desconto) + "\n",
     "salario liquido:" + str(salario_liquido))