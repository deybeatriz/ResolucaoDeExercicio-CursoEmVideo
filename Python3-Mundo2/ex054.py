# 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
anoatual = date.today().year

menor = 0
maior = 0
tem18 = 0

for c in range(1, 8):
    anonasc = int(input(f'{c}) Em que ano vc nasceu? '))
    idade = anoatual - anonasc

    if idade > 18:
        maior += 1
    elif idade < 18:
        menor += 1
    else:
        tem18 +=1

print('\n{} pessoa(s) são maiore(s) de  idade \n{} pessoa(s) são menore(s) de idade \n{} pessoa(s) têm 18 anos.'.format(maior, menor, tem18))

