# 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Insira um número: '))
d = 0

for c in range (1, n+1):
    if n % c == 0:
        d += 1
if d == 2:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')