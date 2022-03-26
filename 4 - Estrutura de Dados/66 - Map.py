# A função map() é para realizar funções com listas. Aplica uma função a um interable, por item (lista, tupla, dicionário)

lista1 = [1,2,3,4]

def multi(x): #definindo uma função de multiplicar um argumento por 2. 
    return x*2

print(multi(4)) #Passando o valor x para a função de multiplicar 

# Para utilizar a função na lista, utiliza-se o map:

lista2 = map(multi, lista1) #O primeiro argumento é o nome da função e o segundo é a lista

print(list(lista2)) #A função 'list' é para converter o objeto map em uma lista. 