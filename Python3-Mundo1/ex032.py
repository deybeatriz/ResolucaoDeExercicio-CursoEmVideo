# 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Insira um ano: '))

print(f'\nO  ano {ano} é bissexto? ')
print('sim' if ano % 4 == 0 else 'não')