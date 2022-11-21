# 045 - Crie um programa que faça o Computador jogar Jokenpô com você.
from random import randint

print('='*20, 'JOKENPÔ', '='*20)
print('\nVamos lá! Escolha: \n[1] PEDRA \n[2] PAPEL \n[3] TESOURA')

player = int(input('\nQual a opção? '))

cp = randint(1, 3)

if player == 1:
    if cp == 3:
        print('Você escolheu PEDRA, eu escolhi TESOURA! Você ganhou, parabéns!')
    elif cp == 2:
        print('Você escolheu PEDRA, eu escolhi PAPEL! Você perdeu hahaha')
    else:
        print('Ambos escolhemos PEDRA, empatamos! Vamos mais uma vez...')

elif player == 2:
    if cp == 1:
        print('Você escolheu PAPEL, eu escolhi PEDRA! Você ganhou, parabéns!')
    elif cp == 3:
        print('Você escolheu PAPEL, eu escolhi TESOURA! Você perdeu hahaha')
    else:
        print('Ambos escolhemos PAPEL, empatamos! Vamos mais uma vez...')

if player == 3:
    if cp == 2:
        print('Você escolheu TESOURA, eu escolhi PAPEL! Você ganhou, parabéns!')
    elif cp == 1:
        print('Você escolheu TESOURA, eu escolhi PEDRA! Você perdeu hahaha')
    else:
        print('Ambos escolhemos TESOURA, empatamos! Vamos mais uma vez...')

elif player != 1 and player != 2 and player != 3:
    print('Jogada inválida! Tente novamente.')
