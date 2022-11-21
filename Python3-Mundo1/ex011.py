# 011 -  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

b = float(input('Insira a largura da parede em metros: '))
h = float(input('Insira a altura da parede em metros: '))
area = b * h

print('\nSua parede tem a dimensão de {}x{}, a sua área é igual a {}'.format(b, h, area))
print('Para pintar essa parede você precisa de {} litros de tinta.'.format(area/2))