# 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s = float(input('Qual o seu salário atual? '))

print('Seu salário, após o rajuste, fica em R${}.'.format(s + (s * 15/100)))