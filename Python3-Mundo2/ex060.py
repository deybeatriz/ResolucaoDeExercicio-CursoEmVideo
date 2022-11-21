# 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

a = int(input('Insira um número para ver o seu fatorial: '))
f = 1
print(f'{a}! = ', end=' ')

while a > 0:
    f *= a
    if a > 1:
        print('{} x'. format(a), end=' ')
    elif a == 1:
        print('{} = '. format(a), end='')
    f -= 1
print(f)
