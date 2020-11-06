#opção de voltar pro inicio nos menus

from tabela import escolher_tabela
from acao import escolher_acao

# cria um menu para o usuário escolher sobre qual tabela quer trabalhar
tabela = escolher_tabela()

# cria um menu para o usuário escolher qual ação executar sobre a tabela
escolher_acao(tabela)