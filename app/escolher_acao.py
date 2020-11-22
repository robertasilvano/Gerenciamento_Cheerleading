from sql import select_query, insert_query, select_index, select_nome_descricao

# cria um menu para o usuário escolher a ação a ser executada sobre a tabela escolhida
def escolher_acao(tabela, col_selecionadas_query, col_selecionadas_vetor):
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
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}\n')
        acao_select(tabela, col_selecionadas_query, col_selecionadas_vetor)

    elif acao_escolhida == 2:
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}\n')
        acao_insert(tabela, col_selecionadas_query, col_selecionadas_vetor)

    elif acao_escolhida == 3:
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}\n')
        acao_update(tabela, col_selecionadas_query, col_selecionadas_vetor)

    elif acao_escolhida == 4:
        print(f'Você escolheu a opção [{acao_escolhida}] - {acao_dict[acao_escolhida]}\n')
        acao_delete(tabela, col_selecionadas_query, col_selecionadas_vetor)

    else:
        print('\nOpção inválida! Escolha novamente.')
        escolher_acao(tabela, col_selecionadas_query, col_selecionadas_vetor)

def acao_select(tabela, col_selecionadas_query, col_selecionadas_vetor):

    # verifica se foi selecionada alguma coluna. se sim, define a query, e chama a função pra fazer o select no banco
    if col_selecionadas_query:
        query = f'SELECT {col_selecionadas_query} FROM {tabela}'
        df = select_query(query, col_selecionadas_vetor)
        print('RESULTADO: ')
        print(df)

def acao_insert(tabela, col_selecionadas_query, col_selecionadas_vetor):

    id_tabela = 'id_' + tabela
    if id_tabela in col_selecionadas_vetor:
        index = select_index(tabela)

    for col in col_selecionadas_vetor:
        if ('id_' in col) and (f'id_{tabela}' not in col):
            #id primario

            tabela_estrangeira = col.replace('id_', '')

            
            tabela_nome = ['atleta', 'contato_Emergencia', 'medicamento']
            if tabela_estrangeira in tabela_nome:
                query = f'SELECT {col}, nome FROM {tabela_estrangeira}'

            else:
                query = f'SELECT {col}, descricao FROM {tabela_estrangeira}'

            df_tabela_estrangeira = select_nome_descricao(query)
            print('\n')
            if df_tabela_estrangeira.empty:
                print(f'A tabela estrangeira {tabela_estrangeira} está vazia. Não é possível fazer a inserção.')
                #### chamar inicio
            else:
                print(f'\nSeguem os códigos da tabela {tabela_estrangeira} abaixo: ')
                print(df_tabela_estrangeira.to_string(header=False, index=False))

    # usuário insere os valores que devem ir pro banco
    values = []
    print('INSIRA OS VALORES: ')
    for col in col_selecionadas_vetor:
        if f'id_{tabela}' in col:
            print('Id preenchido automaticamente')
            values.append(index+1)
        else:
            value = input(f'{col.upper()}: ')
            values.append(value)

    values = str(values).replace('[', '').replace(']', '')
    if values:
        try: 
            query = f'INSERT INTO {tabela} ({col_selecionadas_query}) values ({values})'
            print(query)
            df = insert_query(query, col_selecionadas_vetor)
        except:
            print('\nVocê inseriu um valor com formato errado. Insira novamente: ')
            acao_insert(tabela, col_selecionadas_query, col_selecionadas_vetor)

def acao_update(tabela, col_selecionadas_query, col_selecionadas_vetor):
    print('u')
def acao_delete(tabela, col_selecionadas_query, col_selecionadas_vetor):
    print('d')