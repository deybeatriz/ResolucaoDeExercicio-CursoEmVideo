# 020 - O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = str(input('Insira o nome do primeiro aluno: '))
aluno2 = str(input('Insira o nome do segundo aluno: '))
aluno3 = str(input('Insira o nome do terceiro aluno: '))
aluno4 = str(input('Insira o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)  #Shuffle = Embaralha os itens de uma lista

print('A ordem de apresentação será {}'.format(lista))

# apenas é embaralhada a lista existente, não é criada outra, atente-se!