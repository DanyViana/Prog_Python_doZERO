from funcoes import somar
from funcoes import multiplicar

#from cadastro import cliente - não vai funcionar dessa forma pois ele só enxerga o que está no mesmo nível dele. É necessário dentro da pasta de 'Itens' criar um arquivo com o nome '__init__.py' (pode deixar vazio mesmo) para o python identificar que é um packages. 

from item.cadastro import cliente

cliente()

#Não rodou! O arquivo '84 - Packages' deveria estar fora da pasta '6 - Modulos' para funcionar. Tem que ser um arquivo principal dentro do projeto PROG_PYTHON_DOZERO. 