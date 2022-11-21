# 042 -  Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a < (b + c) or b < c + a or c < a + b:
    print('\nOs segmentos podem formar um triângulo', end=' ')

    if a == b == c:
        print('equilátero')
    elif a == b or a == c:
        print('isósceles')
    else:
        print('escaleno')

else:
    print('Os segmentos não podem formar um triângulo.')