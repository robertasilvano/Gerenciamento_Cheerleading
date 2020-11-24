from sql import select_query, insert_query, select_index, select_nome_descricao, get_column_names, delete_query, update_query
from escolher_colunas import colunas_all

# cria um menu para o usuário escolher a ação a ser executada sobre a tabela escolhida
def escolher_acao(tabela, col_selecionadas_query, col_selecionadas_vetor):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

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
        print(f'Você escolheu a opção {bold_underline}[{acao_escolhida}] - {acao_dict[acao_escolhida]}{end_bold_underline}')
        acao_select(tabela, col_selecionadas_query, col_selecionadas_vetor)

    elif acao_escolhida == 2:
        print(f'Você escolheu a opção {bold_underline}[{acao_escolhida}] - {acao_dict[acao_escolhida]}{end_bold_underline}')
        acao_insert(tabela, col_selecionadas_query, col_selecionadas_vetor)

    elif acao_escolhida == 3:
        print(f'Você escolheu a opção {bold_underline}[{acao_escolhida}] - {acao_dict[acao_escolhida]}{end_bold_underline}')
        acao_update(tabela, col_selecionadas_query, col_selecionadas_vetor)

    elif acao_escolhida == 4:
        print(f'Você escolheu a opção {bold_underline}[{acao_escolhida}] - {acao_dict[acao_escolhida]}{end_bold_underline}')
        acao_delete(tabela, col_selecionadas_query, col_selecionadas_vetor)

    else:
        print(f'\n{bold_underline}Opção inválida! Escolha novamente.{end_bold_underline}')
        escolher_acao(tabela, col_selecionadas_query, col_selecionadas_vetor)

def acao_select(tabela, col_selecionadas_query, col_selecionadas_vetor):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    # define a query, e chama a função pra fazer o select no banco
    query = f'SELECT {col_selecionadas_query} FROM {tabela}'
    df = select_query(query, col_selecionadas_vetor)
    print(f'{bold_underline}RESULTADO: {end_bold_underline}')

    if not df.empty:
        print(df)

    else:
        print('Essa tabela está vazia\n')


    # COLOCAR AQUI UM inicio()


def acao_insert(tabela, col_selecionadas_query, col_selecionadas_vetor):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    id_tabela = 'id_' + tabela
    if id_tabela in col_selecionadas_vetor:
        index = select_index(tabela)

    for col in col_selecionadas_vetor:
        # verifica se é chave estrangeira. se for, não deverá ser preenchida automaticamente.
        if ('id_' in col) and (f'id_{tabela}' not in col):

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
                print(f'\nSeguem os códigos da tabela {bold_underline}{tabela_estrangeira}{end_bold_underline} abaixo: ')
                print(df_tabela_estrangeira.to_string(header=False, index=False))

    # usuário insere os valores que devem ir pro banco
    values = []
    print('\nINSIRA OS VALORES: ')
    for col in col_selecionadas_vetor:
        if f'id_{tabela}' in col:
            print(F'{bold_underline}Id preenchido automaticamente{end_bold_underline}')
            values.append(index+1)
        else:
            value = input(f'{col.upper()}: ')
            values.append(value)

    values = str(values).replace('[', '').replace(']', '')
    if values:
        try: 
            query = f'INSERT INTO {tabela} ({col_selecionadas_query}) values ({values})'
            df = insert_query(query, col_selecionadas_vetor)
        except:
            print('\nVocê inseriu um valor com formato errado. Insira novamente: ')
            acao_insert(tabela, col_selecionadas_query, col_selecionadas_vetor)

def acao_update(tabela, col_selecionadas_query, col_selecionadas_vetor):

    print('\nA tabela que você deseja dar update possui os seguintes dados: ')
    colunas_query, colunas_vetor = colunas_all(tabela)
    query = f'SELECT {colunas_query} FROM {tabela}'
    df_all = select_query(query, colunas_vetor)
    df_all = df_all.to_string(index=False)

    if df_all:
        print(df_all)
    else:
        print('Essa tabela está vazia\n')

    condition = int(input(f'\nInsira o id do registro(id_{tabela}) que você deseja dar update: '))
    print(condition)

    print('Insira os valores atualizados: ')
    values = []    
    for col in col_selecionadas_vetor:
        if f'id_{tabela}' in col:
            col_selecionadas_vetor.remove(col)
            values.append(value)

    query = f'UPDATE {tabela} SET '
    cont = 0
    for col in col_selecionadas_vetor:
        print(col)
        print(values[cont])
        query = query + f'{col} = {values[cont]}'
        cont += 1

    update_query(query)


def acao_delete(tabela, col_selecionadas_query, col_selecionadas_vetor):
    print('\nA tabela que você deseja deletar contem os seguintes dados: ')
    colunas_query, colunas_vetor = colunas_all(tabela)
    query = f'SELECT {colunas_query} FROM {tabela}'
    df_all = select_query(query, colunas_vetor)
    df_all = df_all.to_string(index=False)
    if df_all:
        print(df_all)
    else:
        print('Essa tabela está vazia\n')

    ldel = int(input('Insira o indentificador(id) do item que deseja deletar: '))
    
    lverif = str(input(f'\nTem certeza que deseja deletar a linha {ldel}? Y/N' ))
    if(lverif == N or lverif == n):
        escolher_acao(tabela, col_selecionadas_query, col_selecionadas_vetor)

    
    lquery = f'DELETE FROM {tabela} WHERE id_{tabela} = {ldel}'
    delete_query(lquery)
    print(f'Linha {ldel} deletada com sucesso! uel uel uel uel, novinha o pau de selfie do Bertie está o mel' )
