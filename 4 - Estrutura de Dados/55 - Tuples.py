# Tuples: armazena mais de uma informação em variáveis. Manter a sequência dos dados em uma variável. Não podem ser alteradas - é a maior diferença entre as listas. 

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']

cores_tuples = ('amarelo', 'verde', 'azul', 'vermelho')

# Quase tudo o que você faz com uma lista você faz com uma tuple

print(type(cores_list))
print(type(cores_tuples))

duas_listas = cores_list * 2
print(duas_listas)

duas_tuples = cores_tuples * 2
print(duas_tuples)

cores_list.append('Roxo') #Na tuple não é possível. 

print(cores_list)

# Não é possível alterar qualquer coisa numa tuple! Utilize para itens que serão fixos no seu código. Listas gastam um espaço maior de memória que uma tuple, ou seja, tuples são mais rápidas. 