from datetime import datetime #Para o programa pegar automaticamente o ano atual. 

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento): #init significa que é um contrutor. O self significa que ele vai passar por cada usuário(objeto), é tipo um loop sem ser um loop. 
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
# Dessa forma, não importa quantos objetos tenhamos, ele sempre será trocado pelo self. 

    def nome_completo(self): #Os argumentos já estão na função de cima, por isso não é necessário declarar novamente. 
        return self.nome + ' ' + self.sobrenome   

    def idade_funcionario(self): 
        ano_atual = datetime.now().year #Vai no sistema e puxa qualo ano atual. 
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


usuario1 = Funcionarios('Danielly', 'Viana', 2015)
usuario2 = Funcionarios('Dany', 'Santos', 2020)
usuario3 = Funcionarios('Dani', 'Viana', 2019)

print(usuario1.nome)
print(usuario2.sobrenome)

print(usuario1.nome_completo())
#Esse de cima e esse de baixo são a mesma coisa. 
print(Funcionarios.nome_completo(usuario3))

print(Funcionarios.idade_funcionario(usuario1))