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