# Um looping para percorrer todos os valores que estão na lista. 

valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f' O valor final do produto é de R$ {x}.')


# Verificando itens numa lista
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cor_cliente = input('Digite a cor desejada: ')

cores = ['amarelo', 'verde', 'azul', 'vermelho']
if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Cor não disponível em estoque')
# Como não temos controle como o cliente irá digitar, e como na nossa lista todos os valores estão escritos em letras minúsculas, a função .lower() é para deixar tudo em minúsculo