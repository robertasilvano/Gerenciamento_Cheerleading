'''
FLUXO:
1. Escolher a tabela
2. Escolher a ação
3.1 SELECT/INSERT/UPDATE: Escolher sobre quais colunas quer trabalhar
3.2. DELETE

FAZER:
1. [FEITO] colocar inicio() nos menus, voltar entre os menus
2. [NÃO NECESSÁRIO] ver como faz pra tratar os tipos de dados 
3. [FEITO] ver como faz pra tratar as tabelas do meio na hora de dar insert/delete/update -
4. [FEITO] ver sobre o auto increment
5. [FEITO] negrito
6. [FEITO] verificar se foram inseridas duas colunas com valor igual no escolher_colunas
7. [FEITO] dar uma melhorada na função escolher_colunas
8. [IGNORATED] where no select
8. [IGNORATED] tratativa no insert
10. [FEITO] alterar os dict e o banco de dados p nome do select id
11. [FEITO] mudar no banco cargo pra descricao
12. [FEITO] where no update e delete
13. [FEITO] Ver update/delete nas tabelas do meio kkk
14. [FEITO] Ver colunas not null
15. [FEITO] Ver o q acontece quando insere formato errado
16. [FEITO] Ver o try/except no insert e no delete
17: [FEITO] Fazer mais de um insert/update/delete
18. [FEITO] As tabelas do meio só tão com chave estrangeira
19. Colocar chaves primarias nas tabelas estrangeiras e colocar todas as colunas como not null


valores que podem ser add errados:
TABELA - CAMPO
skill - nivel
atleta - nascimento
projeto - data
falta - data
evento - data
fluxo_caixa - valor, data, flag_entrada_saida

integer/decimal/timestamp
'''

from escolher_tabela import escolher_tabela
from escolher_acao import escolher_acao

def tabelas(flag):
    while flag == 'Play':
        tabela, flag = escolher_tabela()

    return tabela

def acao(tabela, flag):
    while flag == 'Play':
        flag = escolher_acao(tabela)
    
    if flag == 'Tabelas':
        main()

def main():
    flag = 'Play'
    tabela = tabelas(flag)
    flag = 'Play'
    acao(tabela, flag)

main()