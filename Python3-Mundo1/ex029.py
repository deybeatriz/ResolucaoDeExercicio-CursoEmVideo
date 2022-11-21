# 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print('\nMULTADO! Você ultrapassou a velocidade permitida que é de 80km/h')
    print('Você deve pagar uma multa de RS{:.2f}'.format((vel - 80) * 7))

else:
    print('Ótimo!')

print('\nTenha um bom dia! Diija com segurança!')