# Imprimir uma sequência de números:

for numero_1 in range(5):
    print(numero_1)
print('\n')

#Para variável dentro da quantidade de vezes que o for loop vai girar dentro de si mesmo. 

#Ele começa pelo index 0. 

for numero_2 in range(1, 5): #Start em 1 e stop em 4
    print(numero_2)
print('\n')

for numero_3 in range(1, 10, 3): #Start em 1, stop em 9 e step de 3 em 3
    print(numero_3)
print('\n')

# Para letras:

for letra_1 in 'Danielly':
    print(letra_1)
print('\n')

palavra = 'Python'
for letra_2 in palavra:
    print(f'{letra_2} está dentro da palavra {palavra}') #usando a formated string (aula 20)

# Modificando a palavra PYTHON para P Y T H O N
palavra = 'PYTHON'

for espaco in palavra: 
    print(espaco + ' ', end='') #esse end faz com que ele não pule uma linha no looping, ele continue na mesma linha
    

for espaco in palavra: 
    print(f' {espaco}', end='') #forma de escrever usando a formated string