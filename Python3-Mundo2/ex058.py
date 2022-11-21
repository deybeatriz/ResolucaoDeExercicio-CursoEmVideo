# Melhore o jogo do DESAFIO 28 onde o Computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('=-' * 28 )
print('Vou pensar em um número de 0 a 10. Tente advinhar...')
print('=-' * 28)

player = int(input('\nEm que número eu pensei? '))
comp = randint(0,10)
tentativas = 0

while player != comp:
    player = int(input('\nVocê errou haha! Tente novamente.\nEm que número eu pensei? '))
    tentativas += 1
    if comp > player:
        'Mais...'
    elif comp < player:
        print('Menos...')
print(f'\nVocê acertou! Foram necessárias {tentativas} tentativas para chegar ao resultado correto.')


#Forma diferente by Youtube
from random import randint
from time import sleep

print('\n' + '\033[1;37m-=-'*18)
print('\033[34m    Vou pensar em um número aleatório entre 0 e 10')
print('\033[37m-=-'*18)
print('\033[4;97mVocê vai ter 3 chances para tentar advinhar...')

n = 1
try:
    while n == 1:
        n1 = randint(0, 10)
        n2 = int(input('\n\033[mEm que número eu pensei? '))
        if n2 > 10:
            print('\n\033[4mNúmero Inválido')
            exit()
        sleep(0.5)

        cont = 0
        lim = 2

        while n1 != n2 and cont != lim:
            if n2 < n1:
                print('\033[1;31mERROU! É mais...')
            else:
                print('\033[1;31mERROU! É menos...')
            n2 = int(input(f'\033[m({lim - cont} chances) Tente mais uma vez: '))

            if n2 > 10:
                print('\n\033[4mNúmero Inválido')
                exit()

            cont += 1

        if cont == lim and n1 != n2:
            print(f'\033[1;31mSuas chances acabaram, você perdeu!\033[m)\n(O número que eu pensei era o {n1})\n')
        else:
            print(f'\033[1;32mACERTOU! Você precisou de {cont + 1} tentativas para vencer!')

        print('''\033[1;37mVocê quer continuar jogando?\033[m
        
    [\033[36m1\033[m] Sim
    [\033[36m0\033[m] Não''')

        n = int(input('Digite a sua opção: '))
        if n != 0:
            while n != 0 and n != 1:
                print('''\033[4;31mResposta Inválida\033[m
                
    \033[1;37mVocê quer continuar jogando?\033[m
    [\033[36m1\033[m] Sim
    [\033[36m0\033[m] Não''')
                n = int(input('Digite a sua opção: '))
        print('\033[37m-'*25)

except ValueError:
    print('\033[4;31mResposta Inválida\033[m')
print('\033[mAté mais!')