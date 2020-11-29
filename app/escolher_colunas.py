from sql import get_column_names

# seleciona todas colunas da tabela escolhida, e cria um menu para o usuário selecionar quais colunas quer realizar a ação
def escolher_colunas(tabela):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    # pega o nome das colunas, cria o menu, e pega o input 
    df_colunas = get_column_names(tabela)

    col_id = ''
    print(f'\nÉ possível selecionar as seguintes {bold_underline}colunas da tabela {tabela}{end_bold_underline}. [Colunas id são selecionadas automaticamente]: ')
    print('[*] - Todas')
    for index, row in df_colunas.iterrows():
        if 'id_' not in row['Coluna']:
          print('[{0}] - {1}'.format(index, row['Coluna']))
        else:
          print('[{0}] - {1}'.format(index, row['Coluna']))
          col_id = col_id + str(index)
    print(f'[{index+1}] - Voltar ao menu de tabelas')
    print(f'[{index+2}] - Voltar ao menu de ações')
    
    col_selecionadas_num = input(f'\nInsira o número das colunas que você deseja selecionar no formato {bold_underline}número_coluna1, número_coluna2, etc. Por exemplo: 1, 2, 3{end_bold_underline} [Valores inválidos são ignorados]:')
    print('\n')

    if str((index+1)) in col_selecionadas_num:
      print(f'\nVocê selecionou: {bold_underline}[{index+1}] - Voltar ao menu de tabelas{end_bold_underline}') 
      return None, 'Tabelas'
    if str((index+2)) in col_selecionadas_num:
      print(f'\nVocê selecionou: {bold_underline}[{index+2}] - Voltar ao menu de ações{end_bold_underline}') 
      return None, 'Ações'
    
    col_selecionadas_num = col_selecionadas_num + col_id

    qtd_colunas_max = len(df_colunas.index)

    # o usuário selecionou as colunas desejadas por números, mas é necessário transforma-los nas string correspondentes
    col_selecionadas_vetor = []
    if '*' in col_selecionadas_num:
      for cont in range(qtd_colunas_max):
        col_selecionadas_vetor.append(df_colunas.iloc[cont]['Coluna'])
    else:
      for cont in range(qtd_colunas_max):
        if str(cont) in col_selecionadas_vetor:
          continue
        if str(cont) in col_selecionadas_num:
          col_selecionadas_vetor.append(df_colunas.iloc[cont]['Coluna'])

    print(f'\nAs colunas que você selecionou foram: {bold_underline}{col_selecionadas_vetor}{end_bold_underline}') 

    # limpa o vetor pra ficar no formato da query do sql
    col_selecionadas_query = ', '.join(col_selecionadas_vetor)

    return col_selecionadas_query, None

def colunas_all(tabela):
  # pega o nome das colunas, cria o menu, e pega o input 
    df_colunas = get_column_names(tabela)

    col_selecionadas_num = '*'
    qtd_colunas_max = len(df_colunas.index)

    col_selecionadas_vetor = []
    for cont in range(qtd_colunas_max):
      col_selecionadas_vetor.append(df_colunas.iloc[cont]['Coluna'])

    col_selecionadas_query = str(col_selecionadas_vetor).replace('[', '').replace(']', '').replace('\'', '')

    return col_selecionadas_query