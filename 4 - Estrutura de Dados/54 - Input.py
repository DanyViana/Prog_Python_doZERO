# Criar uma lista de frutas a partir de informações digitadas pelo usuário

frutas_usuario = input ('Digite o nome das frutas separados por vírgula: ')

print(frutas_usuario)
# Retorna fora de uma lista.

frutas_lista = frutas_usuario.split(', ')
# Split é a função que vai separar a cada vez que ele vê uma vígula e um espaço  . 

print(frutas_lista)
