# Um looping dentro do outro. 

for num1 in range (5):
    print(num1)
    for num2 in range(3):
        print(num2)

#Começa com o 0 do primeiro for, ai entra no 0 a 2 do segundo for, ai vai para o 1 do primeiro for, ai entra no 0 a 2 do segundo for, e assim por diante. 

for num_1 in range (1,5):
    print('Produto ' + str(num_1))
    for num_2 in range(3):
        print(num_1,num_2)
