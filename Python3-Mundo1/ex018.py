# 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo que você deseja: '))
ang_rad = radians(ang)
# Para calcular seno, cosseno e tangente, utilizando essa biblioteca, os valores precisam estar em radiano (de acordo com a documentação)

print('\nO ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(ang_rad)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(ang_rad)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(ang_rad)))