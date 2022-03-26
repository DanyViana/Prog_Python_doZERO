# Função filter: muito utilizada com listas.

valores = [10,20,33,45,101]

def remover20(x): #Uma função para retornar apenas os valores maiores que 20. 
    return x>20

print(list(map(remover20,valores))) #Vai retornar com true ou false, de acordo com a análise da função. 

print(list(filter(remover20,valores))) #Vai retornar os valores da lista. 

print(list(filter(lambda x: x>20,valores))) #Utilizando a função lambda não é necessário definir uma função (as linhas 5 e 6 podem ser desconsideradas). Achei a função lambda um pouco bagunçada, prefiro definir uma função para deixar mais organizado. A lambda é bom pois reduz a quantidade de linhas de código. 

