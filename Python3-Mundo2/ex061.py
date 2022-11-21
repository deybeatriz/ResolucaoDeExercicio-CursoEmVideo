# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

PrimeiroTermo = int(input('Insira o primeiro termo da PA: '))
Razao = int(input('Insira a razão da PA: '))
Limite = 0

while Limite < 10:
    print(f'{PrimeiroTermo} ->', end=' ')
    PrimeiroTermo += Razao
    Limite += 1
print('fim :)')