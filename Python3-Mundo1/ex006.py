# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

a = int(input('Insira um número: '))
print(f'O dobro de {a} é {a * 2}')
print(f'O triplo de {a} é {a * 3}')
print('A raiz quadrada de {} é {:.2f}'.format(a, a ** (1/2)))