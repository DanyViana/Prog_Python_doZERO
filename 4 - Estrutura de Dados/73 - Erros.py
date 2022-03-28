# Erros: Excelente para testes. Não realiza o 'stop' no programa. Mensagem customizada quando encontrar um erro. Excelentes para o caso do usuário digitar um input incorreto. 

try:
    teste = ['a', 'b', 'c']

    print(teste[3]) # Mostra uma mensagem de erro pois não tem esse index na lista e ele pararia o programa nessa linha e não executaria o restante do código. 
except IndexError:
    print('Index não existe')

# Para isso, é necessário incluir o tray e o except. 

try:
    valor = int(input('Digite o valor do produto: '))
    print(valor)
except ValueError: 
    print('Por gentileza, informe valores numéricos para o produto.')
else: 
    print('Valor informado corretamente.')
    resultado = valor * 2 
    print(resultado)

print('mais código abaixo')

#No lugar do else também podemos utilizar o 'finally', ele será executado independente se deu erro ou não no código. 