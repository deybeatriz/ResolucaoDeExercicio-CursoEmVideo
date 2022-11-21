# 024 -  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Insira o nome de uma cidade: '))lower().strip().split(' '). #strip = rmove espaços antes e depois /split: divide uma string e coloca como elementos em um lista
cidade = cidade[0]

print('santo' in cidade)