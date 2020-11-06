from sql import get_column_names, select_query, insert_query

# seleciona todas colunas da tabela escolhida, e cria um menu para o usuário selecionar quais colunas quer realizar a ação
def escolher_colunas(tabela):
    # pega o nome das colunas, cria o menu, e pega o input
    df_colunas = get_column_names(tabela)

    print('\nÉ possível selecionar as seguintes colunas: ')
    for index, row in df_colunas.iterrows():
        print('[{0}] - {1}'.format(index, row['Coluna']))

    col_selecionadas_num = input('\nInsira o número das colunas que você deseja selecionar. [Insira todos os números sem dar enter. Valores inválidos são ignorado] ')
    #### como tratar valores errados??
    #### colocar opção pra *

    qtd_colunas_max = len(df_colunas.index)

    # o usuário selecionou as colunas desejadas por números, mas é necessário transforma-los nas string correspondentes
    col_selecionadas_vetor = []
    for cont in range(qtd_colunas_max):
        if str(cont) in col_selecionadas_num:
            col_selecionadas_vetor.append(df_colunas.iloc[cont]['Coluna'])

    # limpa o vetor pra ficar no formato da query do sql
    col_selecionadas_query = str(col_selecionadas_vetor).replace('[', '').replace(']', '').replace('\'', '')

    return col_selecionadas_query, col_selecionadas_vetor

def acao_select(tabela):

    # seleciona todas colunas da tabela escolhida, e cria um menu para o usuário selecionar quais colunas quer realizar a ação
    col_selecionadas_query, col_selecionadas_vetor = escolher_colunas(tabela)

    # verifica se foi selecionada alguma coluna. se sim, define a query, e chama a função pra fazer o select no banco
    if col_selecionadas_query:
        query = f'SELECT {col_selecionadas_query} FROM {tabela}'
        df = select_query(query, col_selecionadas_vetor)
        print('RESULTADO: ')
        print(df)

def acao_insert(tabela):
    # seleciona todas colunas da tabela escolhida, e cria um menu para o usuário selecionar quais colunas quer realizar a ação
    col_selecionadas_query, col_selecionadas_vetor = escolher_colunas(tabela)

    # usuário insere os valores que devem ir pro banco
    values = []
    print('INSIRA OS VALORES: ')
    for col in col_selecionadas_vetor:
        value = input(f'{col.upper()}: ')
        values.append(value)
    #####tem que tratar aqui os tipos de dados e dar auto increment pros ids
    
    print(values)
    values = str(values).replace('[', '').replace(']', '')
    print(values)
    if values:
        query = f'INSERT INTO {tabela} ({col_selecionadas_query}) values ({values})'
        print(query)
        df = insert_query(query, col_selecionadas_vetor)
        print('RESULTADO: ')
        print(df)

def acao_update(tabela):
    print('u')
def acao_delete(tabela):
    print('d')

def escolher_acao(tabela):

    # cria um dicionário das ações possíveis
    acao_dict = {
        1: 'SELECT',
        2: 'INSERT',
        3: 'UPDATE',
        4: 'DELETE'
    }
    
    # cria o menu das opções de ações disponíveis
    print('OPÇÕES DE AÇÕES: ')
    for acao in acao_dict:
        print(f'[{acao}] - {acao_dict[acao]}')

    acao_escolhida = int(input('\nEscolha a ação desejada: '))

    # verifica qual ação foi escolhida e chama a função da mesma
    if acao_escolhida == 1:
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}')
        acao_select(tabela)

    elif acao_escolhida == 2:
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}')
        acao_insert(tabela)

    elif acao_escolhida == 3:
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}')
        acao_update(tabela)

    elif acao_escolhida == 4:
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}')
        acao_delete(tabela)

    else:
        print('\nOpção inválida! Escolha novamente.')
        escolher_acao(tabela)