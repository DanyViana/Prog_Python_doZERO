# Use operador ternário para reduzir as linhas de códigos. 

# Exemplo de uma idade para ser permito votar

idade = int(input('Digite sua idade: ')) #o int é para transformar em inteiro
print(idade)

if idade >=16:
    print('Voto permitido')
else:
    print('Voto não permitido')

# Esse é o jeito mais comum de fazer, com 4 linhas de código. Mas temos o seguinte jeito abaixo com apenas 1 linha de código: 

resultado = 'Voto permitido' if idade >=16 else 'Voto não permitido'

print(resultado)