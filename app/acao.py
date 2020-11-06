from sql import select_colunas, select_query

def acao_select(tabela):
    # seleciona todas colunas da tabela escolhida, e cria um menu para o usuário selecionar quais colunas quer dar o select
    df_colunas = select_colunas(tabela)

    print('\nÉ possível selecionar as seguintes colunas: ')
    
    for index, row in df_colunas.iterrows():
        print('[{0}] - {1}'.format(index, row['Coluna']))

    col_selecionadas_num = input('\nInsira o número das colunas que você deseja selecionar. [Inserir todos os números sem dar enter.] ')
    #### como tratar valores errados??

    qtd_colunas_max = len(df_colunas.index)

    # o usuário selecionou as colunas desejadas por números, mas é necessário transforma-los nas string correspondentes
    col_selecionadas_vetor = []
    for cont in range(qtd_colunas_max):
        if str(cont) in col_selecionadas_num:
            col_selecionadas_vetor.append(df_colunas.iloc[cont]['Coluna'])

    # limpa o vetor pra ficar no formato da query do sql
    col_selecionadas_query = str(col_selecionadas_vetor).replace('[', '').replace(']', '').replace('\'', '')

    # verifica se foi selecionada alguma coluna. se sim, define a query, e chama a função pra fazer o select no banco
    if col_selecionadas_query:
        query = f'SELECT {col_selecionadas_query} FROM {tabela}'
        df = select_query(query, col_selecionadas_vetor)

    print('RESULTADO: ')
    print(df)


def acao_insert(tabela):
    print('i')
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