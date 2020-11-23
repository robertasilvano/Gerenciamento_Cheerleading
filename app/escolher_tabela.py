from sql import get_table_names
import pandas as pd

def escolher_tabela():
    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    # cria um df com todas as tabelas disponiveis no banco de dados
    df_tabelas = get_table_names()

    # percorre o df_tabelas, para criar um menu e o usuário escolher a tabela desejada
    print('OPÇÕES DE TABELA: ')
    for index, row in df_tabelas.iterrows():
        print(f'[{index}] - ' + row['Tabela'])
    
    tabela_escolhida = int(input('\nEscolha a tabela desejada: '))

    # trata valores inválidos
    if tabela_escolhida < 0 or tabela_escolhida > 22:
        print(f'{bold_underline}Você escolheu um valor inválido. Escolha novamente: {end_bold_underline}\n')
        escolher_tabela()

    print(f'Você escolheu a tabela {bold_underline}[{tabela_escolhida}] - ' + df_tabelas.iloc[tabela_escolhida]['Tabela'] + f'{end_bold_underline}\n')

    # retorna o nome da tabela escolhida
    return df_tabelas.iloc[tabela_escolhida]['Tabela']
