# É possível utilizar mais de um operador de compraração. Vamos ao exemplo de uma loja que vende produtos com os preços entre $20 e $40. Valores fora desse intervalo não são aceitos nessa loja. 

valor = int(input('Digite o valor do seu produto: '))

if valor >=20 and valor < 40: #Pode ser escrito como 20 <= valor < 40, com isso você executa a variável valor apenas 1x - código mais limpo!  
    print('Mercadoria pode ser comercializada.')
else:
    print('Mercadoria não pode ser comercilizada nessa loja!')

