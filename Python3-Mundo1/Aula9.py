# Operações com String

# Fatiamento
'''
frase = 'Curso em Vídeo Pthon'

slice:
frase[9]  # Ele vai buscar o caractere localizado na posição 9
frase[9, 21]  # Vai me mostrar os itens localizados a partir da posição 9 até a posição 20
frase[9, 21, 2]   # Vai me mostrar os itens localizados a partir da posição 9 até a posição 20, porém, pulando de 2 em 2 caracteres]
frase[:5]   # Vai me mostrar todos os caracteres até a posição 4
frase[15:]   # Vai me mostrar todos os caracteres a partir do 15 até o final
frase[9::3]   # Vai me mostrar do caractere 9 até o finla, mas pulando de 3 em 3 caracteres

'''


# Análise
'''
len(frase)  # Analisa o comprimento da frase 
frase.count('o')   # Analisa quantas vezes o 'o' aparece na frase
frase.count('o', 0, 13)   # Analisa quantas vezes o 'o' aparece na frase, já com o fatiamento de 0 a 13
frase.find('deo')   # Indica em que posição é encontrada "deo"
'curso' in frase   # Vai analisar se a palavra curso existe na frase
'''

# Transformação
'''
frase.replace('Python', 'Android')   # Troca a palavra Python por Android
frase.strip()   # Remove espaços antes e depois
frase.rstrip()  # Remove os espaços da direita
frase.lstrip()  # Remove os espaços da esquerda 
'''

# Divisão
'''
frase.split()   # Vai dividir uma string (Por padrão, nos espaços), e colocar como elementos em um lista
>>> ['Curso', 'em', 'Vídeo', 'Python']
'''

# Junção

'''
Se vc tem itens dipostos em um lista, vc pode juntá-los da seguinte forma:

'-'.join(frase)
>>> Curso-em-Video-Python
'''
