# 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Digite um número: '))
print(f'O valor digitado foi {num}, a sua parte inteira é igual a {trunc(num)}.')

# Ainda pode ser feito de outra forma:
print(f'O valor digitado foi {num}, a sua parte inteira é igual a {int(num)}.')
