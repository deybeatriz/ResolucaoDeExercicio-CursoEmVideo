# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media_idade = 0
maior_idade = 0
m_maior20 = 0
nome_maior_idade= ''

for c in range(1, 5):
    nome = str(input(f'Qual o nome da {c}ª pessoa? ')).capitalize().strip()
    idade = int(input(f'Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? [F/M] ')).upper().strip()
    print('')

    media_idade += idade
    if sexo == 'M':
        if idade > maior_idade:
            nome_maior_idade = nome.capitalize()
    elif sexo == 'F':
        if idade > 20:
            m_maior20 += 1

print('A média de idade do grupo é {:.2f} anos. '.format(media_idade/4))
print(f'O homem mais velho se chama {nome_maior_idade}')
print(f'{m_maior20} mulheres têm mais de 20 anos.')