aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for x in aluno:
    print(x) #Impressão das keys

#Outro jeito de escrever seria: for x in aluno.keys()

for x in aluno.values(): 
    print(x) #Impressão dos valores

for x in aluno.items():
    print(x) #Impressão dos itens do dicionário

for keys, values in aluno.items():
    print(keys,values)

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True, 'materias': ['física','matemática','biologia']}
print(aluno)

#Jeito mais bonitinho de organizar:
aluno = {
    'nome': 'Ana',
    'idade': 16,
    'nota_final': 'A',
    'aprovação': True,
    'materias': ['física','matemática','biologia']
    }
print(aluno.get('materias'))

print(len(aluno)) #Retorna ao número de keys que tem no dicionário

#