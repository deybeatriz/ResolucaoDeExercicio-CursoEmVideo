# 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()   # strip = Remove espaços antes e depois

print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras.'.format((len(nome) - nome.count(' '))))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))   # find = indica em que posição está o que vc procura, lembrando que a primeira posição é 0.

