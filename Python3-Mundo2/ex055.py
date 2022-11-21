# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


 REFAZER!!!!


maior = 0
menor = 0
outro = 0

for c in range(1, 6):
    peso = float(input(f'{c}) Qual o seu peso? '))

    if c == 1:
        maior = c
        menor = c
    else:
        if peso >= maior:
            maior = peso
        if menor <= peso:
            menor = peso

print(f'O maior peso lido foi {maior}kg. \nO menor peso lido foi {menor}')