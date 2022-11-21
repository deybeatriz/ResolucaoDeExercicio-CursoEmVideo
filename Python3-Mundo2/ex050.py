# 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

par = 0
s = 0

for c in range(1, 7):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        par += 1
        s += n

print(f'\n{par} dos números inseridos são pares. A soma entre eles é igual a {s}')