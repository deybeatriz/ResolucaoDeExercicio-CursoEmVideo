# 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
print('')

for pa in range(0, 10):
    print(a1, end=' -> ')
    a1 += r
print(' fim :)')