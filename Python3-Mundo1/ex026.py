# 026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Insira uma frase: ').lower())

print('Quantas vezes a letra "a" aparece? {}'.format(frase.count('a')))
print('A primeira letra "a" aparece na posição {}'.format(frase.find('a') + 1))
print('A primeira letra "a" aparece na posição {}'.format(frase.rfind('a') + 1))
