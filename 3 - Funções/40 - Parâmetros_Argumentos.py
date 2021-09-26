# Uma loja que quer falar com os seus clientes:

def boas_vindas(nome, quantidade): #dentro do () vão ter os parâmetros
    print(f'Olá, {nome}.')
    print(f'Temos {str(quantidade)} PCs disponíveis.')


boas_vindas('Dany',5) #quando chamar a função você defini quais os parâmetros que ela deve chamar. 
boas_vindas('Gafanhoto',10)
boas_vindas('Pessoa',2)

def quantidades_deful(nome, quantidade = 6): #dentro do () vão ter os parâmetros, o parâmetro de quantidade é default, não será alterado. E o de nome será no-default. 
    #Sempre coloque na seguinte ordem: parâmetros no-default e depois os default
    print(f'Olá, {nome}.')
    print(f'Temos {str(quantidade)} PCs disponíveis.')

quantidades_deful('Dani') #se eu não definir ele vai vim como 6
quantidades_deful('teste', 4) #se eu definir o parâmetro de quantidade ele subescreve

def mais_de_uma(nome, quantidade = 3, local = 'almrep'): #dentro do () vão ter os parâmetros
    print(f'Olá, {nome}.')
    print(f'Temos {str(quantidade)} PCs disponíveis no {local}.')

mais_de_uma('Dani', 2 , 'almox')

def cliente1(nome):
    print(f'Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'

# x = cliente1('Maria') #Coloquei como comentário porque fica apontando o erro
y = cliente2('José')

# print(x) #Retorna como 'none' pois a função print só realiza uma tarefa - retorna um valor na tela, mas no programa em si não retorna nada
print(y) #A função return calcula e retorna um valor (fica armazenado)
