# Uma loja que quer falar com os seus clientes:

def boas_vindas(nome, quantidade): #dentro do () vão ter os parâmetros
    print(f'Olá, {nome}.')
    print(f'Temos {str(quantidade)} PCs disponíveis.')


boas_vindas('Dany',5) #quando chamar a função você defini quais os parâmetros que ela deve chamar. 
boas_vindas('Gafanhoto',10)
boas_vindas('Pessoa',2)