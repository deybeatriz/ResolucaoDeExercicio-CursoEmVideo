# 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Insira a frase: ')).upper().strip().split()
junto =''.join(frase)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

if junto == inverso:
    print('A frase "{}" é um palíndromo.'.format(' '.join(frase)))
else:
    print('A frase "{}" não é um palíndromo.'.format(' '.join(frase)))