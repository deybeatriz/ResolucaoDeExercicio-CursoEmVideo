# 062 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

PrimeiroTermo = int(input('Insira o primeiro termo da PA: '))
Razao = int(input('Insira a razão da PA: '))
MaisTermos = 10
TermosMostrados = 0

while MaisTermos != 0:
    Limite = 1
    while Limite <= MaisTermos:
        print(f'{PrimeiroTermo} ->', end=' ')
        PrimeiroTermo += Razao
        Limite += 1
        TermosMostrados += 1
    print('PAUSA')
    MaisTermos = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'\nForam mostrados {TermosMostrados} termos.')