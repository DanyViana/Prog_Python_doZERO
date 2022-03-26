# Erros: Excelente para testes. Não realiza o 'stop' no programa. Mensagem customizada quando encontrar um erro. 

try:
    teste = ['a', 'b', 'c']

    print(teste[3]) # Mostra uma mensagem de erro pois não tem esse index na lista e ele pararia o programa nessa linha e não executaria o restante do código. 
except IndexError:
    print('Index não existe')

# Para isso, é necessário incluir o tray e o except. 
