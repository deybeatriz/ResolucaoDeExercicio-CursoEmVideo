# 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
from math import sqrt

cat_o = float(input('Insira o valor do cateto oposto: '))
cat_a = float(input('Insira o valor do cateto adjacente: '))
hipo = sqrt((cat_a**2) + (cat_o**2))

print('A hipotenusa vai medir {:.2f}'.format(hipo))
'''

# Solução dada pelo professor:

from math import hypot

cat_o = float(input('Insira o valor do cateto oposto: '))
cat_a = float(input('Insira o valor do cateto adjacente: '))
hipo = hypot(cat_a, cat_o)

print('A hipotenusa vai medir {:.2f}'.format(hipo))