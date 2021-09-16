# No exemplo será trabalhado o envio de um e-mail de confirmação da compra online (máximo 3 tentativas) para compras confirmadas.

compra_confirmada = False #fique trocando entre True e False
dados_compra = 'Compra no valor de $12 e entrega confirmada.'

for enviar in range(3): #enviar é a variável e no range tem as 3 tentativas
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail.')
        break #sai fora se a compra for confirmada
    else:
        print('Falha na compra!')
        break

