# List Comprehension: utilizando quando você precisa criar uma nova lista a partir de uma já existente. 

frutas1 = ['banana', 'abacaxi', 'manga', 'uva', 'morango']
frutas2 = [] #vazia pois vamos adicionar conteúdo depois
 
for iten in frutas1: #para cada item dentro da lista de frutas1
    if 'b' in iten:  #quando tiver a letra 'b' no item
        frutas2.append(iten) #acrescente dentro da lista frutas2

print(frutas2)

# Esse mesmo resultado em uma única linha de código: 

frutas3 = [iten for iten in frutas1 if 'b' in iten]

print(frutas3)

# Com números:

valores = []

for x in range(6):
    valores.append(x*10)

print(valores)

# Esse mesmo resultado em uma única linha de código: 

valores2 = [x*10 for x in range(6)]

print(valores2)
 