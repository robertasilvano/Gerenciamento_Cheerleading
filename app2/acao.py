from sql import select

def acao_select(tabela, colunas):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    # define a query, e chama a função pra fazer o select no banco
    query = f'SELECT {colunas} FROM {tabela}'
    colunas = colunas.split(',')
    df_select = select(query, colunas)
    print(f'\n{bold_underline}RESULTADO: {end_bold_underline}\n')

    if not df_select.empty:
        print(df_select.to_string(index=False))
        print('\n')

    else:
        print('Essa tabela está vazia\n')