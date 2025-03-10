"""
Programa: parte 1. exercicio 14
Descrição: calcule a distˆancia entre dois pontos de coordenadas, respectivamente, (x1, x2) e (x1, x2).
Tais coordenadas devem ser lidas do teclado. Use a formula da distancia euclideana entre
dois pontos.
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""
# entrada de dados
coordenada_1 = []
coordenada_2 = []

# armazenamento de dados
for i in range(2):
    x_1 = float(input(f"coordenada 1, x{i+1}: "))
    coordenada_1.append(x_1)

for i in range(2):
    x_2 = float(input(f"coordenada 2, x{i+1}: "))
    coordenada_2.append(x_2)

# processamento de dados
hipotenusa = (((coordenada_1[0] - coordenada_2[0])**2) + ((coordenada_1[1] - coordenada_2[1])**2))**(1/2)
hipotenusa

#saida de dados
print(f"para as coordenadas ({coordenada_1[0]}, {coordenada_1[1]}) e ({coordenada_2[0]}, {coordenada_2[1]}), a distancia entre os pontos é {hipotenusa}")
    