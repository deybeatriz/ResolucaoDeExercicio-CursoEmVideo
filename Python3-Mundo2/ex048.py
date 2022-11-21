# 048 - Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
n = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        n += 1
print(f'A soma dos {n} números mútiplos de 3 entre 1 e 500, é igual a {s}.')