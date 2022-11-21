'''
Aula 14 – Estrutura de repetição while

for - utilize quando souber o limite
while - quando não souber o limite
'''

for c in range(1, 10):
    print(c)

# é a mesma coisa que o seguinte programa:

c = 1
while c < 10:
    print(c)
    c += 1

# outro exemplo:

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()















