# Listas
# Colocar vários dados dentro de uma mesma variável 
# Toda lista é entre []
# Manter a sequencia dos dados em uma variável 

cidades = ['Rio de Janeiro', 'São Paulo', 'Fortaleza'] 
# Uma variável com 3 cidades, que começam no index 0

print(cidades)

numeros = [2, 6, 10] #é possível usar números nas listas

print(numeros)

# Para puxar apenas um item de uma lista: 
print(cidades[0]) #entre [] fica  index da lista
print(cidades[-1]) #-1, -2, -3... é da direita para a esquerda

# Os index são: 
    # Da esquerda para a direita: 0, 1, 2, 3...
    # Da direita para a esquerda: -1, -2, -3...

# Para mudar um valor de uma lista: 
cidades[0] = 'Brasília'

print(cidades)

# Existem várias funções para manipulação de listas. Dá uma googada! 

cidades.append ('Santa Catarina') #vai para o final da lista. Adiciona no final da lista. 

print(cidades)

cidades.remove('São Paulo') #remover um item da lista

print(cidades)

cidades.insert(1, 'Morro de São Paulo') #insere exatamente na posição que você quer

print(cidades)

cidades.pop(0) #retira de acordo com o index informado

print(cidades)

cidades.sort() #organiza em ordem alfabética

print(cidades)