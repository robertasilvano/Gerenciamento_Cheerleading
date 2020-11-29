from sql import select, select_index, insert, update, delete
from escolher_colunas import colunas_all
from tabela_estrangeira import tabela_estrangeira
import psycopg2

def acao_select(tabela, colunas):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'


    # define a query, e chama a função pra fazer o select no banco
    id_tabela = 'id_' + tabela
    query = f'SELECT {colunas} FROM {tabela} ORDER BY {id_tabela}'
    colunas_vetor = colunas.split(', ')
    df_select = select(query, colunas_vetor)
    print(f'\n{bold_underline}RESULTADO: {end_bold_underline}\n')

    if not df_select.empty:
        print(df_select.to_string(index=False))
        print('\n')

    else:
        print(f'{bold_underline}Essa tabela está vazia{end_bold_underline}\n')
    
    input('\nPressione enter para continuar\n')
    return 'Tabelas'

def acao_insert(tabela, colunas):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    # define o vetor onde serão inseridos os valores
    values = []

    # define a chave primária para tabelas das beiradas
    id_tabela = 'id_' + tabela
    if id_tabela in colunas:
        index = select_index(tabela)

    print(f'{bold_underline}A tabela {tabela}, que você deseja fazer inserção possui os seguintes dados:{end_bold_underline}')
    acao_select(tabela, colunas)
    colunas_vetor = colunas.split(', ')
    tabela_estrangeira(colunas_vetor, tabela, id_tabela, 'a inserção!')

    # usuário insere os valores que devem ir pro banco
    print('\nINSIRA OS VALORES: ')
    for col in colunas_vetor:
        # verifica se é a coluna chave primária da tabela das beiradas. Se for, preenche automaticamente com o index.
        if col == id_tabela:
            print(F'{bold_underline}Identificador {id_tabela} preenchido automaticamente{end_bold_underline}')
            values.append(index+1)

        elif ('id_' in col) and (col != id_tabela):
            value = int(input(f'{col.upper()} [CHAVE ESTRANGEIRA]: '))
            values.append(value)

        else:
            value = input(f'{col.upper()}: ')
            values.append(value)

    values = str(values).replace('[', '').replace(']', '')
    if values:
        try: 
            query = f'INSERT INTO {tabela} ({colunas}) values ({values})'
            insert(query, colunas_vetor)
            print('Insert realizado com sucesso!')
            
            verif = str(input(f'\n Deseja dar insert em outro registro desta mesma tabela? [Y/N] ' ))
            if(verif == 'Y' or verif == 'y'):
                acao_insert(tabela, colunas)
            else:
                input('\nPressione enter para continuar\n')
                return 'Tabelas'
        except psycopg2.Error as e:
            if e.pgcode == '22007':
                print(f'\nVocê inseriu um campo de data com o formato errado. Insira novamente no formato {bold_underline}dd/mm/aaaa{end_bold_underline}.')
                input('\nPressione enter para continuar\n')
                acao_insert(tabela, colunas)
            elif e.pgcode == '22P02':
                print(f'\nVocê inseriu um campo de número com o formato errado. Insira novamente.')
                input('\nPressione enter para continuar\n')
                acao_insert(tabela, colunas)
            elif e.pgcode == '22001':
                print(f'\nVocê inseriu caracteres demais em um campo. Insira novamente.')
                input('\nPressione enter para continuar\n')
                acao_insert(tabela, colunas)
            elif e.pgcode == '23503':
                print(f'\nVocê inseriu um valor inválido de ID. Insira novamente.')
                input('\nPressione enter para continuar\n')
                acao_insert(tabela, colunas)
            elif e.pgcode == '23505':
                print(f'\nEsse valor já está na tabela. Insira outro.')
                input('\nPressione enter para continuar\n')
                acao_insert(tabela, colunas)
            else:
                print('Ocorreu algum erro! Retornando para o menu de tabela!\n')
                input('\nPressione enter para continuar\n')
            return 'Tabelas'

def acao_update(tabela, colunas):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    id_tabela = 'id_' + tabela

    print(f'\n{bold_underline}A tabela que você deseja dar update possui os seguintes dados: {end_bold_underline}')
    colunas_query = colunas_all(tabela)
    query = f'SELECT {colunas_query} FROM {tabela}'
    colunas_vetor = colunas_query.split(', ')
    df_all = select(query, colunas_vetor)

    if not df_all.empty:
        print(df_all.to_string(index=False))
    else:
        print('Essa tabela está vazia, não é possível fazer update!\n')
        input('Pressione enter para continuar\n')
        return 'Tabelas'

    condition = []
    if id_tabela in colunas_vetor:
        value = int(input(f'\nInsira o id do registro {bold_underline}({id_tabela}){end_bold_underline} que você deseja dar update: '))
        condition.append(value)
    else:
        for coluna in colunas_vetor:
            value = int(input(f'\nInsira o id do registro {bold_underline}({coluna}){end_bold_underline} que você deseja dar update: '))
            condition.append(value)

    tabela_estrangeira(colunas_vetor, tabela, id_tabela, 'o update!')

    colunas_selecionadas_vetor = colunas.split(', ')
    print('Insira os valores atualizados: ')
    values = []    
    for col in colunas_selecionadas_vetor:
        if col == id_tabela:
            print(f'{col.upper()}: {bold_underline} Você não possui permissão para alterar o identificador{end_bold_underline}')
            
        else:
            value = input(f'{col.upper()}: ')
            values.append(value)
        
    count = 0
    query = f'UPDATE {tabela} SET '
    for col in colunas_selecionadas_vetor:
        if col == id_tabela:
            continue
        else:
            query = query + f'{col} = \'{values[count]}\', '
            count += 1

    query = query[:-2]
    count = 0
    if id_tabela in colunas_vetor:
        query = query + f' WHERE id_{tabela} = {condition[count]}'
    else:
        query = query + 'WHERE '
        for item in colunas_vetor:
            query = query + f'{item} = {condition[count]} AND '
            count+=1
        query = query[:-5]

    try:
        update(query)
        print('Update realizado com sucesso!')
        verif = str(input(f'\n\n Deseja dar update em outro registro desta mesma tabela? [Y/N] ' ))
        if(verif == 'Y' or verif == 'y'):
            acao_update(tabela, colunas)
        else:
            input('\nPressione enter para continuar\n')
            return 'Tabelas'
    except psycopg2.Error as e:
            if e.pgcode == '22007':
                print(f'\nVocê inseriu um campo de data com o formato errado. Insira novamente no formato {bold_underline}dd/mm/aaaa{end_bold_underline}.')
                input('\nPressione enter para continuar\n')
                acao_update(tabela, colunas)
            elif e.pgcode == '22P02':
                print(f'\nVocê inseriu um campo de número com o formato errado. Insira novamente.')
                input('\nPressione enter para continuar\n')
                acao_update(tabela, colunas)
            elif e.pgcode == '22001':
                print(f'\nVocê inseriu caracteres demais em um campo. Insira novamente.')
                input('\nPressione enter para continuar\n')
                acao_update(tabela, colunas)
            else:
                print('Ocorreu algum erro! Retornando para o menu de tabela!\n')
                input('\nPressione enter para continuar\n')
            return 'Tabelas'
    
def acao_delete(tabela):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    id_tabela = 'id_' + tabela

    print(f'\nA tabela {tabela} contem os seguintes dados: ')
    colunas_query = colunas_all(tabela)
    query = f'SELECT {colunas_query} FROM {tabela}'
    colunas_vetor = colunas_query.split(', ')
    df_all = select(query, colunas_vetor)
    
    if not df_all.empty:
        print(df_all.to_string(index=False))
    else:
        print('Essa tabela está vazia, não é possível realizar um delete!\n')
        input('Pressione enter para continuar\n')
        return 'Tabelas'

    condition = []
    if id_tabela in colunas_vetor:
        value = int(input(f'\nInsira o id do registro {bold_underline}({id_tabela}){end_bold_underline} que você deseja deletar: '))
        condition.append(value)
    else:
        for coluna in colunas_vetor:
            value = int(input(f'\nInsira o id do registro {bold_underline}({coluna}){end_bold_underline} que você deseja deletar: '))
            condition.append(value)
  
    verif = str(input(f'\nTem certeza que deseja deletar {bold_underline}{id_tabela} = {condition}{end_bold_underline}? [Y/N] ' ))
    if(verif == 'N' or verif == 'n'):
        return 'Tabelas'
    
    if id_tabela in colunas_vetor:
        query = f'DELETE FROM {tabela} WHERE {id_tabela} = {condition[0]}'
    else:
        count = 0
        query = f'DELETE FROM {tabela} WHERE '
        for item in colunas_vetor:
            if 'id_' in item:
                query = query + f'{item} = {condition[count]} AND '
                count+=1
        query = query[:-5]

    try:
        delete(query)
        if id_tabela in colunas_vetor:
            print(f'{bold_underline}{id_tabela} = {condition}{end_bold_underline} deletada com sucesso!\n')
        else:
            print(f'{bold_underline}{condition}{end_bold_underline} deletada com sucesso!\n')
        verif = str(input(f'\n Deseja deletar outro registro desta mesma tabela? [Y/N] ' ))
        if(verif == 'Y' or verif == 'y'):
            acao_delete(tabela)
        else:
            input('\nPressione enter para continuar\n')
            return 'Tabelas'
    except psycopg2.Error as e:
        if e.pgcode == '22P02':
                print(f'\nVocê inseriu um campo de número com o formato errado. Insira novamente.')
                input('\nPressione enter para continuar\n')
                acao_delete(tabela, colunas)
        elif e.pgcode == '23503':
            tabela_ref = str(e.pgerror).split('\"')[-2]
            print(f'Não é possível deletar essa linha porque está referenciada na tabela {bold_underline}{tabela_ref}{end_bold_underline}.')
            input('\nPressione enter para continuar\n')
        else:
            print('Ocorreu algum erro! Retornando para o menu de tabela!\n')
            input('\nPressione enter para continuar\n')
        return 'Tabelas'

def acao_espec(query, colunas):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    df_select = select(query, colunas)
    print(f'\n{bold_underline}RESULTADO: {end_bold_underline}\n')

    if not df_select.empty:
        print(df_select.to_string(index=False))
        print('\n')

    else:
        print(f'{bold_underline}Essa tabela está vazia{end_bold_underline}\n')
    
    input('\nPressione enter para continuar\n')
    return 'Tabelas'
