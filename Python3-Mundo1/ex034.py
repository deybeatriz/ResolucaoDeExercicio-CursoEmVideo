# 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

valor = float(input('Qual o salário do funcionário? '))
if valor <= 1250.00:
    print('Quem ganhava {} passa a ganhar {} agora.'.format(valor, (valor + (valor * 15/100))))
else:
    print('Quem ganhava {} passa a ganhar {} agora.'.format(valor, (valor + (valor * 10/100))))