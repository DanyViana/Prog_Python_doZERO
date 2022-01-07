#Sets são similares a listas, evitam itens duplicados e não utilizam index. 

lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set (lista2)

print(num1)
print(num2)

print(num1 | num2) #essa barra significa união - unifica as listas retirando os repetidos
print(num1 - num2) #é a diferença - não mostra os repetidos
print(num1 ^ num2) #é o simetrico - retira os duplicados nas duas listas
print(num1 & num2) #mostra o que está duplicado
print(len(num1))