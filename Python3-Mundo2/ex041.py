# 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

anonasc = int(input('Em que ano vc nasceu? '))
atual = date.today().year
idade = atual - anonasc

print(f'O atleta tem {idade} anos.')
print('Sua categoria é', end=' ')

if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Júnior')
elif 19 < idade <= 25:
    print('Sênior')
else:
    print('Master')