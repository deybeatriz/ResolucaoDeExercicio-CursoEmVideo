"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
import time

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('\n','=-' * 25)
    opcao = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa

Qual a sua opção?
           '''))
    print('--'* 25)
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            print(f'A soma entre {a} e {b} é {a + b}')
        elif opcao == 2:
            print(f'A mutiplicação entre {a} e {b} é {a * b}')
        elif opcao == 3:
            if a > b:
                print(f'Entre {a} e {b} o maior valor é {a}')
            elif b > a:
                print(f'Entre {a} e {b} o maior valor é {b}')
            else:
                print(f'Os valores são iguais.')
        elif opcao == 4:
            a = int(input('Insira um novo valor: '))
            b = int(input('Outro valor valor: '))
    else:
        print('Opção inválida! Tente novamente? ')

print('Finalizando...')
time.sleep(0.5)
print('Obrigada por usar o programa! :)')