# Utilizando métodos com as strings

mensagem = 'eu Amo comida Caseira'
mensagem1 = '        eu amo'

print(mensagem)

# Para utilizar um método você coloca a variável, um ponto e o método. 

print(mensagem.lower()) #Tudo com letra minúscula 
print(mensagem.upper()) #Tudo com letra maiúscula
print(mensagem.capitalize()) #Coloca a primeira letra em maiúsculo
print(mensagem.find('c')) #Encontra um caractere e retorna em qual posição ele está
print(mensagem.find('C')) #É case sensitive
print(mensagem.find('Amo')) #Retorna o index no qual a palavra começa
print(mensagem.find('amo')) #Vai retornar como -1 porque não achou essa palavra
print(mensagem.replace('a','e')) #Colocar o antigo e o novo, o que eu quero trocar e o que eu quero colocar no lugar 
print(mensagem.replace('Caseira','feita em casa')) #Troca palavras também 
print(mensagem1)
print(mensagem1.strip()) #Remove qualquer espaço que tem antes do primeiro caractere

#Coloque o ponto após a variável, escolha e veja o help para descobrir as possibilidades de métodos. 