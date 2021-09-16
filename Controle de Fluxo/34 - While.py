# Criar uma promoção para um produto que custa R$ 100 e a cada dia que passa ele reduz R$ 5,00. O produto custa R$ 20, não pode vender a menos que R$ 20,00. 

valor = 100 #valor do produto
dia = 1

while valor > 20: #enquanto o valor for maior que 20, imprima o valor:
    print(f'No dia {dia} o produto vai ser vendido por R${valor}')
    dia += 1 #vai acrescentar um dia a cada giro do while
    valor -=5 #vai tirar 5 do valor a cada giro dentro do while

# Perfeito para girar um loop enquanto você tem uma condição. Excelente para loops dependentes de uma condição. 