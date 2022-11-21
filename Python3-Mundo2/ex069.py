# 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

Mais18 = QuantidadeM = Mais20F = 0

while True:

    sexo = ' '
    Continua = ' '

    idade = int(input('Insira a sua idade: '))
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0]

    if idade >= 18:
        Mais18 += 1
    if sexo == 'M':
        QuantidadeM += 1
    if sexo == 'F' and idade < 20:
        Mais20F += 1

    while Continua not in 'SN':
        Continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        print('-' * 30)
    if Continua == 'N':
        break

    print('Dados da próxima pessoa: ')

print('-' * 30)
print(f'{Mais18} pessoas têm mais de 18 anos. \n{QuantidadeM} homens foram cadastrados no sistema. \n{Mais20F} das mulheres cadastradas têm menos de 20 anos.')