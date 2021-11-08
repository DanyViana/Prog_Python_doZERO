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

numeros = [2,3,4,5]
final = numeros * 2 # Vai duplicar a lista
print(final)

letras = ['a', 'b', 'c', 'd']
final2= numeros + letras # Concatenar listas
print(final2)

numeros.extend(letras) # Estendeu a lista de números com a lista de letras
print(numeros)

itens = ['item1', 'item2', 'item3', 'item4']
print(itens)

itens2 = [['item1', 'item2'], ['item3', 'item4']]
# Uma lista dentro de outra lista, a lista maior tem dois index (0 e 1), e as sublistas também tem dois index (0 e 1)

print(itens2[0][1]) # Retorna ao valor do index 0 da lista maior na posição 1

produtos = ['arroz', 'feijão', 'laranja', 'banana']
item1 = produtos[0]
print(item1)

item1, item2, item3, item4 = produtos # Todas as variáveis associadas a lista
print(item1)
print(item2)
print(item3)
print(item4)

produtos2 = ['arroz', 'feijão', 'laranja', 'banana', 2, 3, 4]
item1, item2, item3, *outros = produtos2 # Para referenciar apenas alguns dos itens da lista
print(item1)
print(item2)
print(item3)
print(outros)

produtos3 = ['arroz', 'feijão', 'laranja', 'banana', 2, 3, 4]
item1, item2, *outros, item6 = produtos3 # Para referenciar apenas alguns dos itens da lista
print(item1)
print(item2)
print(outros)
print(item6)