# 063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
TENTAR OUTRA HORA
#termos = int(input('Quantos termos você quer mostrar? '))
termos =1
a = 0
b = 1
while termos < 10:

    print(f'{a} ->', end=' ')
    a += b
    b += a
    termos +=1