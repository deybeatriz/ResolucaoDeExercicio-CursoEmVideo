# 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Quanto você recebe por mês? '))
ano = int(input('Em quantos anos pretende pagar? '))
prestação = casa/ (12 * ano)

print('\nPara pagar um imóvel de {:.2f} em {} anos a prestação será de {:.2f}'.format(casa, ano, prestação))

if prestação > (30/100 * salario):
    print('Infelizmente seu empréstimo não foi aprovado!')
else:
    print('Parabéns! Seu empréstimo foi aprovado.')