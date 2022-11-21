# 068 - Faça um programa que jogue par ou ímpar com o Computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 18)
print('VAMOS JOGAR: PAR OU ÍMPAR?')
print('=-' * 18)

Contador = 0

while True:
    Numero = int(input('Jogue um valor: '))
    Computador = randint(0, 10)
    Soma = Numero + Computador
    ParImpar = ' '
    SomaParImpar = Soma % 2

    while ParImpar not in 'PI':
        ParImpar = str(input('Par ou Ímpar? ')).upper().strip()[0]
    print('-' * 45)

    if SomaParImpar == 0:
        print(f'Você jogou {Numero} e eu joguei {Computador}. Total de {Soma}, PAR.')
    else:
        print(f'Você jogou {Numero} e eu joguei {Computador}. Total de {Soma}, ÍMPAR.')
    print('-' * 45)

    if ParImpar == 'P' and SomaParImpar == 0:
        print('Você venceu! \nVamos jogar novamente.')
        print('-' * 45)
        Contador += 1
    elif ParImpar == 'I' and SomaParImpar == 1:
        print('Você venceu! \nVamos jogar novamente.')
        print('-' * 45)
        Contador += 1
    else:
        print(f'GAME OVER! Você venceu {Contador} vezes.')
        break