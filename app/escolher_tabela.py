from sql import get_table_names
import pandas as pd

def escolher_tabela():
    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    # cria um df com todas as tabelas disponiveis no banco de dados
    df_tabelas = get_table_names()
    qtd_tables = len(df_tabelas.index)

    # percorre o df_tabelas, para criar um menu e o usuário escolher a tabela desejada
    print(f'{bold_underline}OPÇÕES DE TABELA: {end_bold_underline}')
    for index, row in df_tabelas.iterrows():
        print(f'[{index}] - ' + row['Tabela'])
    print(f'[{qtd_tables+1}] - Sair')
    
    # pega o input do usuário
    tabela_escolhida = int(input('\nEscolha a tabela desejada: '))

    # trata os valores
    if tabela_escolhida == qtd_tables+1:
        print(f'Você escolheu [{tabela_escolhida}] - Sair')
        print('Encerrando o programa')
        exit()
    elif tabela_escolhida < 1 or tabela_escolhida > qtd_tables:
        print(f'{bold_underline}Você escolheu um valor inválido. Escolha novamente: {end_bold_underline}\n')
        return None, 'Play'

    print(f'Você escolheu a tabela {bold_underline}[{tabela_escolhida}] - ' + df_tabelas.at[tabela_escolhida, 'Tabela'] + f'{end_bold_underline}\n')

    # retorna o nome da tabela escolhida
    return df_tabelas.at[tabela_escolhida, 'Tabela'], 'Stop'