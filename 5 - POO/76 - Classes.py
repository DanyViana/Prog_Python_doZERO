# Classes: utilizadas para criar Objetos (intances). Objetos são partes dentro de uma Classe (instancias). Classes são utilizadas para agrupar dados e funções, podendo reutilizar.
# EX: Classe: fruta | Objeto: Banana, maçã...

class Funcionarios: #A primeira letra da classe tem que ser maiúscula 
    #Digitar 'pass' deixa a classe vazia. 
    nome = 'Danielly'
    sobrenome = 'Viana'
    data_nascimento = '28/03/2022'

usuario1 = Funcionarios() #Criação do objeto
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)

#O sentido de criar essa classe foi só para mostrar a criação de uma classe, um objeto e como que chama ela. É interessante utilizar classe inserindo funções nela. 

#Criando a classe
class Funcionarios2: 
    pass

#Criando o objeto
usuario2 = Funcionarios2()
usuario3 = Funcionarios2()

#Criando os parâmetros
usuario2.nome = 'Danielly'
usuario2.sobrenome = 'Viana'
usuario2.data_nascimento = '28/03/2022'

#Criando os parâmetros
usuario3.nome = 'Lúcia'
usuario3.sobrenome = 'Fátima'
usuario3.data_nascimento = '28/03/2022'

print(usuario2.nome)
print(usuario3.data_nascimento)

#Dessa forma possibilita adicionar um novo usuário. 
