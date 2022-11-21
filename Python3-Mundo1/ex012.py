# 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pi = float(input('Insira o preço atual R$'))

print('O produto que custava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}'.format(pi, pi - (pi * 5/100)))
