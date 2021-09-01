# Slice serve para selecionar apenas uma parte da string

fruta = 'Abacate' #definindo uma variável 
# index  0123456
# A posição é definida pelo index e inicializa em 0!

print(fruta)

# Se queremos apenas a letra C da palavra:
print(fruta[3])

# Se queremos um conjunto de letras:
print(fruta[2:5]) #esses dois pontos representa o "de...até", mas ele sempre considera o ínicio (index 2) mas não considera o último (index5, irá considerar o 4)

print(fruta[3:6])

print(fruta[-1])
#index negativo é -1,-2,-3,-4,-5,-6,-7

# Vamos considerar um problema que seja necessário considerar apenas os centavos dos valores:
valor = 99.75
# index 01234

valor_conv = str(valor) #é necessário converter em string

print(valor_conv[3:5]) #se você fizer isso com a variável 'valor' é apresentado o erro de que não é possível fazer com floot, por isso a conversão para string. Não tem o index na variável, mas colocamos ele para que seja considerado até o 4. 

print(valor_conv[:2]) #de qualquer coisa até o index 2.
print(valor_conv[2:]) #de 2 até o final