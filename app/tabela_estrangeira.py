from sql import select_tabela_estrangeira

def tabela_estrangeira(colunas_vetor, tabela, id_tabela, acao):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    for col in colunas_vetor:
        # verifica se é chave estrangeira. se for, não deverá ser preenchida automaticamente, e fará algumas outras verificações.
        if ('id_' in col) and (col != id_tabela):

            # define a tabela estrangeira de onde a chave vem
            tabela_estrangeira = col.replace('id_', '')

            # tratativa
            tabela_nome = ['atleta', 'contato_Emergencia', 'medicamento']
            if tabela_estrangeira in tabela_nome:
                colunas_estrangeira = [col, 'Nome']
                query = f'SELECT {col}, nome FROM {tabela_estrangeira} order by {col}'
            else:
                colunas_estrangeira = [col, 'Descrição']
                query = f'SELECT {col}, descricao FROM {tabela_estrangeira} order by {col}'

            # da um select na tabela estrangeira
            df_tabela_estrangeira = select_tabela_estrangeira(query, colunas_estrangeira)
            print('\n')

            # se a tabela estrangeira estiver vazia, não será possível fazer uma inserção pq não terá a chave estrangeira.
            if df_tabela_estrangeira.empty:
                print(f'A tabela estrangeira {bold_underline}{tabela_estrangeira}{end_bold_underline} está vazia. Não é possível fazer {acao}\n')
                input('\nPressione enter para continuar\n')
                exit()
            # se a tabela estrangeira tiver dados, vai printar os dados para o usuário pegar o código de referencia.
            else:
                print(f'{bold_underline}A tabela {tabela} possui chave estrangeira!{end_bold_underline} Seguem os códigos da tabela de referência {bold_underline}{tabela_estrangeira}{end_bold_underline} abaixo: ')
                print(df_tabela_estrangeira.to_string(index=False))
    
    return