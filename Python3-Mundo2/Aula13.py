# Aula 13 – Estrutura de repetição for

'''
for c in range(1, 6):  # O comando não considera o último número, ou seja, repete 5 vezes.
print('Oi')


for c in range(6, 0, -1):  # O último número indica o que será feito no final do laço
    print(c)


for c in range(0, 10, 2):  # O último número indica o que será feito no final do laço
    print(c)

n = int(input('Digite um número: '))
for c in range(1, n + 1):
    print(c)

for c in range(0, 3):
    n = int(input('Digite um valor: ')


s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n   # a mesma coisa que s = s + n
print(f'O somatório de todos os valores foi {s}')
'''