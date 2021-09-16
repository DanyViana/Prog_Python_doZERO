# Criar uma promoção para um produto que custa R$ 100 e a cada dia que passa ele reduz R$ 5,00. O produto custa R$ 20, não pode vender a menos que R$ 20,00. 

valor = 100 #valor do produto
dia = 1

while valor > 20: #enquanto o valor for maior que 20, imprima o valor:
    print(f'No dia {dia} o produto vai ser vendido por R${valor}')
    dia += 1 #vai acrescentar um dia a cada giro do while
    valor -=5 #vai tirar 5 do valor a cada giro dentro do while

# Perfeito para girar um loop enquanto você tem uma condição. Excelente para loops dependentes de uma condição. 

# Nossa loja revende produtos de outros. Se o valor for acima de R$ 20, teremos uma comissão de 10%. 

valor2 = int(input ('Digite o valor do seu produto em R$: ')) #esse int é para converter a string digitada em inteiro. Mesmo que ele tenha digitado números, o py entende como uma string. Por isso devemos transformar em inteiro. 

while valor2 > 20: 
    valor2 = (valor2 * 0.10) + valor2 #outra forma de fazer seria: valor = 1,1 * valor. Isso é para colocar a comissão de 10% em cima do valor. 
    #GENTE, PRESTATENÇÃO!!!! o Py não entende 0,10! Ele entende 0.10! 
    print(f'O valor final do seu produto será de R$ {valor2}.') 
    break #colocar para não gerar um loop infinito 
