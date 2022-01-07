# Array é semelhante a uma lista, mas com uma performance melhor. É bom para muitos dados. 

from array import array
# É necessário importar pois não é nativo do python. 

letras = ['a', 'b', 'c', 'd']
numeros_inteiros = [10, 20, 30, 40]
numeros_float = [1.2, 2.2, 3.2]

print(letras)
print(numeros_inteiros)
print(numeros_float)
print() #esse print é só para separar 

letras_array = array ('u', ['a', 'b', 'c', 'd']) #Vai no google e pesquisa por python array, vão aparecer os type cods, esse 'u' é tratado como uma string. 
numeros_inteiros_array = array ('i', [10, 20, 30, 40]) #'i' de inteiro 
numeros_float_array = array ('f', [1.2, 2.2, 3.2]) #'f' de float

print(letras_array)
print(numeros_inteiros_array)
print(numeros_float_array)