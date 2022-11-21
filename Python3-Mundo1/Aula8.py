# - Como utilizar módulos em Python
'''
Para importar o módulo completo:
import modulox

Para importar apenas uma função específica da biblioteca:
from bibliotecax import funcaoy

Uma biblioteca muito utilizada para operações matemáticas: MATH

Algumas funcionalidades englobadas na biblioteca math:
ceil - arrendondar p cima (inteiro)
floor - arredondarr p baixo (inteiro)
trunc - truncar (eliminar da vírgula pra frente)
pow - potência
sqrt - raiz quadrada
factorial - fatorial

Exemplo (linha 6 e 7)
Digamos que eu não queira utilizar toda a biblioteca math, quero apenas calcular a raiz quadrada de um número x:
from math import sqrt

Caso eu queira utilizar duas ou três funções, mas ainda assim não quero importar toda a biblioteca:
from math import sqrt, ceil


'''

#Exemplo prático

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))


#ou pode ser feito da seginte forma:

from math import sqrt

num = int(input('Digite um número: ))
raiz = sqrt(num)  #aqui não precisa mais mencionar a biblioteca

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))



# Você pode consultar os detalhes das bibliotecas no documentação python em  https://www.python.org/ > PyPI >
# Segue exemplo do uso de outras bibliotecas


import random

print('{:.2f}'.format(random.random()))   ## random = um número aleatório
print(random.randint(1, 10))              ## randit = um número aleatório dentro de um intervalo fechado

