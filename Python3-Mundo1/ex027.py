# 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Insira seu nome completo: ')).lower().strip().split(' ')
print(nome[0])
print(nome[-1])