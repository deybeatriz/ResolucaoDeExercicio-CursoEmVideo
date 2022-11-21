# 038 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('O PRIMEIRO valor é maior que o segundo. ')
elif b > a:
    print('O SEGUNDO valor é maior que o segundo. ')
else:
    print('Os valores são iguais')