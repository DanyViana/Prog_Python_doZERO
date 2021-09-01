# Para formatar e mostrar uma string podemos fazer de duas formas. A mais longa e uma mais reduzida e simples:

nome = input('Digite seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
profissao = input('Digite a sua profissão: ')

texto = 'O(a) ' + nome + ' ' + sobrenome + ' é um(a) excelente ' + profissao + '.'
print(texto)

texto_facil = f'O(a) {nome} {sobrenome} é um(a) excelente {profissao}.'
print(texto_facil)

# Uma linha de código menor e mais fácil. Usando a Formated String que é o f'', com o texto e as variáveis entre {}