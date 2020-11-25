'''
FLUXO:
1. Escolher a tabela
2. Escolher a ação
3.1 SELECT/INSERT/UPDATE: Escolher sobre quais colunas quer trabalhar
3.2. DELETE
'''

from escolher_tabela import escolher_tabela
from escolher_acao import escolher_acao

def tabelas():
    flag = 'Play'
    while flag == 'Play':
        tabela, flag = escolher_tabela()

    return tabela

def acao(tabela):
    flag = 'Play'
    while flag == 'Play':
        flag = escolher_acao(tabela)

tabela = tabelas()
acao(tabela)