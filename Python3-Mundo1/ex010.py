# 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere o U$1 = R$5,17

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.17

print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
