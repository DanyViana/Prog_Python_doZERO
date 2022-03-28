# Para importar as funções de um outro módulo podemos fazer através de duas formas: import ou from. 

import funcoes

funcoes.somar()
funcoes.multiplicar()

#Para usar o from é da seguinte forma (vou fazer comentado): 
#from funcoes import somar
#somar()

#Nesse caso, ele vai puxar apenas a função somar. 

#from funcoes import * 
#Você vai conseguir puxar todas as funções colocando esse *, mas se forem muitas funções vai ficar lento. 

#from funcoes import somar, multiplicar
#Nesse caso você vai importa mais de uma função 