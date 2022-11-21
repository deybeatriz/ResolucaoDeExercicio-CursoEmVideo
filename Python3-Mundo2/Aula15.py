'''
 Interrompendo repetições while

Laços de repetição

para fazer um "looping infinito",utiliza-se:
while True

para stopar o looping utiliza-se:
break

'''

# exemplo:

n = soma = 0
while True:
    n =int(input('Digite um número: '))
    if n ==999:
        break
    soma += n
print(f'A soma vale {soma}')