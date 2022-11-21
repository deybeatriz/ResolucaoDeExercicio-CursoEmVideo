# 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('=' * 20, 'WAKANDA PET SHOP', '=' * 20)
valor = float(input('Qual o valor da compra? '))

print('\nFORMAS DE PAGAMENTO: \n[1] à vista dinheiro/cheque \n[2] à vista no cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão')
pag = int(input('\nComo deseja pagar? Selecione a opção '))

if pag == 1:
    print('Você ganhou um desconto de 10%! Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(valor, valor - (10/100 * valor)))
elif pag == 2:
    print('Você ganhou um desconto de 5%! Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(valor, valor - (5/100 * valor)))
elif pag == 3:
    print('Sua compra de {} será parcelada em 2x de R${:.2f}'.format(valor, valor/2))
elif pag == 4:
    parc = int(input('Quantas parcelas? '))
    valor_juros = valor + (20/100 * valor)
    print('Sua compra será parcelada em {:2f}x de R${:.2f} com juros, no final ela sairá por R${}'.format(parc,valor_juros/parc, valor_juros))