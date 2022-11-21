# 028 - Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

print('=-' * 28 )
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print('=-' * 28)

teste = int(input('\nEm que número eu pensei? '))
comp = randint(0,5)

print('PROCESSANDO...\n')
sleep(2)

if teste == comp:
    print('PARÁBENS! Você acertou')
else:
    print('HAHA! Você perdeu, eu pensei no número {} e não no {}'.format(comp, teste))
