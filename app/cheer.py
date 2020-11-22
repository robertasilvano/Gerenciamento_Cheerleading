'''
FLUXO:
1. Escolher a tabela
2. Escolher quais colunas quer da tabela especifica
3. Escolher a ação
4. Fazer as ações

FAZER:
1. colocar inicio() nos menus
2. ver como faz pra tratar os tipos de dados -- não tem mais 
3. ver como faz pra tratar as tabelas do meio na hora de dar insert/delete/update -
4. ver sobre o auto increment -- feito
5. negrito
6. verificar se foram inseridas duas colunas com valor igual no escolher_colunas
7. dar uma melhorada na função escolher_colunas
8. where no select
9. voltar entre os menus
10. tratativa no insert
11. alterar os dict e o banco de dados p nome do select id
12. mudar no banco cargo pra descricao
13. where no update e delete
'''

from escolher_tabela import escolher_tabela
from escolher_colunas import escolher_colunas
from escolher_acao import escolher_acao


def inicio():
    # cria um menu para o usuário escolher sobre qual tabela quer trabalhar
    tabela = escolher_tabela()
    
    # seleciona todas colunas da tabela escolhida, e cria um menu para o usuário selecionar quais colunas quer realizar a ação
    col_selecionadas_query, col_selecionadas_vetor = escolher_colunas(tabela)

    # cria um menu para o usuário escolher qual ação executar sobre a tabela
    escolher_acao(tabela, col_selecionadas_query, col_selecionadas_vetor)

inicio()