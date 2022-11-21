#067 – Tabuada v3.0: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0

while True:
    n = int(input('Insira um número para ver a sua tabuada: '))
    print('_' * 20)
    if n < 0:
        break
    for tb in range(1, 11):
        print(f'{n} x {tb} = {n * tb}')
    print('_' * 20)
print('Programa finalizado.')