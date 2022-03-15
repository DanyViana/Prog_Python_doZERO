# Dicionário coloca vários tipos de informações, por exemplo, nas listas é possível colocar as idades de vários alunos, e no dicionário dá para colocar os nomes e as idades, juntos. 
# Utiliza index no formato de Keys e values
# Aceita tudo que é tipo de dado. 
# Um dicionário vazio é {}
# Eles são que nem as listas, são mutáveis, podemos alterar os dados. 

aluno = {'nome':'Dany','idade': 31, 'nota final': 'A', 'status de aprovação': True}
print(aluno)
print(aluno['nome']) #vai imprimir somente o key do nome, se não existir o key vai dar um erro. 

aluno['nome'] = 'José' #atualiza o nome para José
print(aluno)

aluno.update({'nome':'Carlos', 'nota final':'B'}) #adiciono aqui o dicionário, consegue atualizar mais de um campo ao mesmo tempo com uma única linha de código
print(aluno)

aluno.update({'endereço':'Rua A'}) #como o camponão existe ele adicionou no final
print(aluno)

print(aluno.get('nome'))
print(aluno.get('local')) #Retorna que nenhum porque o campo não existe, não mostra um erro
print(aluno.get('local','Não existe')) #é possível configurar uma frase caso não exista

del aluno['idade'] #deletar um campo
print(aluno)