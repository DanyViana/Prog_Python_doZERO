#Sets são similares a listas, evitam itens duplicados e não utilizam index. 

lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(num1)
print(num2)

print(num1 | num2) #essa barra significa união - unifica as listas retirando os repetidos
print(num1 - num2) #é a diferença - não mostra os repetidos
print(num1 ^ num2) #é o simetrico - retira os duplicados nas duas listas
print(num1 & num2) #mostra o que está duplicado
print(len(num1))

s1={1,2,3,4,5,6}
print(s1)
print(type(s1)) #Identifica qual o tipo da variável, nesse caso é um set. 
s1.add(7) #adiciona o item 7 na lista do set
print(s1)

s2={1,2,3,4,5,6,1,2}
print(s2) #Ele não imprime os itens duplicados! 
s2.update([7,8,9]) #adiciona mais de um número 
print(s2)

s2.remove(9) #Se vc remover um número que não está na sua lista ele gera um erro! 
s2.discard(10) #É possível descartar um número que não está na sua lista sem gerar um erro! 
print(s2)

set1={'a','b','c'}
set2={'a','d','e'}
set3={'c','d','f'}

set4=set1.union(set2) #Faz a unificação do set1 com o set2
print(set4) #Remove os duplicados

set5=set1.difference(set3) #Diferença do set1 para com o set3, e não o contrário, por isso só aparece o a e b, não aparece o d e o f. 
print(set5) 

set6=set1.intersection(set2) #O que tem no set1 e tem também no set2, é a interseção
print(set6)

set7=set1.symmetric_difference(set3) #Retira o duplicado e todos os iguais entr
prin