'''
FLUXO:
1. Escolher a tabela
2. Escolher quais colunas quer da tabela especifica
3. Escolher a ação
4. Fazer as ações

FAZER:
1. colocar inicio() nos menus, voltar entre os menus
2. [NÃO NECESSÁRIO] ver como faz pra tratar os tipos de dados 
3. [FEITO] ver como faz pra tratar as tabelas do meio na hora de dar insert/delete/update -
4. [FEITO] ver sobre o auto increment
5. negrito
6. [FEITO] verificar se foram inseridas duas colunas com valor igual no escolher_colunas
7. dar uma melhorada na função escolher_colunas
8. [IGNORATED] where no select
8. [IGNORATED] tratativa no insert
10. [FEITO] alterar os dict e o banco de dados p nome do select id
11. [FEITO] mudar no banco cargo pra descricao
12. where no update e delete
13. Ver colunas not null
'''

from escolher_tabela import escolher_tabela
from escolher_colunas import escolher_colunas
from escolher_acao import escolher_acao

def inicio():
    # cria um menu para o usuário escolher sobre qual tabela quer trabalhar
    tabela = escolher_tabela()
    
    # seleciona todas colunas da tabela escolhida, e cria um menu para o usuário selecionar quais colunas quer realizar a ação
    col_selecionadas_query, col _selecionadas_vetor = escolher_colunas(tabela)

    # cria um menu para o usuário escolher qual ação executar sobre a tabela
    escolher_acao(tabela, col_selecionadas_query, col_selecionadas_vetor)
    
def main():
    sair = False
    while(1):
        sair = inicio()

        if sair == True:
            return

main()