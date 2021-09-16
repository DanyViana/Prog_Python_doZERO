# DRY - Don't repeat yourself. 
# Função foi feita pra você não ter que ficar se repetindo. 

def boas_vindas(): # o "def" é para definir uma função
    print('Olá, Dany.')
    print('Temos 5 PCs disponíveis. Aproveite!')

boas_vindas() # Para chamar a função


def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

#Essas variáveis são somente da função. Não são variáveis globais. Se você não chamar a função, elas não podem ser chamadas se não chamar a função também. Isso possibilita que você copie o código e utilize em outras funções com o mesmo nome de variável, pois como elas são somente da função não terá problema em utilizar o mesmo nome. 

def somar_dois_numeros2():
    numero1 = 5
    numero2 = 20
    resultado = numero1 + numero2
    print(resultado)


somar_dois_numeros()

somar_dois_numeros2()

# As variáveis em cada função tem o mesmo nome, mas é possível fazer isso sem uma mexer na outra, pois são variáveis de cada função, não é uma variável global. 

    

