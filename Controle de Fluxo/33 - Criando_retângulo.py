'''
Criar um retângulo 6x6 que fique da seguinte forma:

@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@

'''

linhas = 6 #quantidade de linhas
colunas = 6 #quantidade de colunas
simbolo = 'o' #o símblo que está formando 

''' Dessa forma ele imprime tudo na vertical
for l in range(linhas): 
    for c in range(colunas):
        print(simbolo)
''' 

''' Dessa forma ele imprime tudo na horizontal
for l in range(linhas): 
    for c in range(colunas):
        print(simbolo, end='')
'''

for l in range(linhas): 
    for c in range(colunas):
        print(simbolo, end='')
    print()

