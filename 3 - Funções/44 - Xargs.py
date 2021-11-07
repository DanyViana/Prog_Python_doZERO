# Não sei quantos argumentos serão, podem ser vários... 

# Criar uma função que soma vários números

def soma (*numeros): #esse * significa que são vários números que podem entrar lá 
    resultado = 0 #é necessário definir inicialmente essa variável, pra lá na soma ele ter com o que começar a somar
    for num in numeros: #como eu não sei a quantidade de variáveis que vão entrar, faço um loop pra ele ficar somando (nesse caso do exemplo com soma). Para cada num dentro dos numeros:
        resultado += num 
    return resultado

x = soma (2,3,4,7)
print(x)

# Criar uma função que armazena números e strings (dados)

def agencia(**carro): #um * é vários argumentos e dois * são vários parâmetros
    return carro

print(agencia (marca='Gol', cor='Branco', motor=1.0)) #retorna um dicionário
print(agencia (marca='Gol', cor='Azul', motor=1.0, placa='ABC123')) 
print(agencia (marca='Gol', cor='Preto', motor=1.5)) 
