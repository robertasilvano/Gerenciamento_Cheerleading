import psycopg2
import pandas as pd


def get_table_names():

    # abre a conexão com o banco
    conn, cursor = connect()

    query = 'SELECT table_name FROM information_schema.tables WHERE table_schema=\'public\' AND table_type=\'BASE TABLE\';'

    # executa a query
    cursor.execute(query)
    tabelas = cursor.fetchall()

    # transforma o resultado em um dataframe 
    df_tabelas = pd.DataFrame(tabelas, columns=['Tabela']).sort_values('Tabela').reset_index()
        
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_tabelas


# seleciona as colunas da tabela escolhida
def get_column_names(tabela):

    # abre a conexão com o banco
    conn, cursor = connect()

    # define a query para selecionar os nomes das colunas
    query = f'SELECT column_name FROM information_schema.columns WHERE TABLE_NAME = \'{tabela}\''

    # executa a query
    cursor.execute(query)
    colunas = cursor.fetchall()

    # transforma o resultado em um dataframe 
    df_colunas = pd.DataFrame(colunas, columns=['Coluna'])
        
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_colunas

def get_column_datatypes(tabela):

    # abre a conexão com o banco
    conn, cursor = connect()

    # define a query para selecionar os nomes das colunas
    query = f'SELECT column_name, data_type FROM information_schema.columns WHERE TABLE_NAME = \'{tabela}\''

    # executa a query
    cursor.execute(query)
    colunas = cursor.fetchall()

    # transforma o resultado em um dataframe 
    df_datatype = pd.DataFrame(colunas, columns=['Coluna', 'Tipo'])
        
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_datatype

# faz o select da tabela e colunas desejadas
def select_query(query, col_selecionadas_vetor):

    # abre a conexão com o banco
    conn, cursor = connect()

    # executa a query
    cursor.execute(query)
    select = cursor.fetchall()

    # transforma o resultado em um dataframe
    df_select = pd.DataFrame(select, columns = col_selecionadas_vetor)
    
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_select

def insert_query(query, col_selecionadas_vetor):
    # abre a conexão com o banco
    conn, cursor = connect()

    # executa a query
    cursor.execute(query)
    conn.commit()
    print('Insert finalizado!')
    
    # fecha a conexão com o banco
    disconnect(conn, cursor)

def select_index(tabela):
     # abre a conexão com o banco
    conn, cursor = connect()
    
    idcon = 'id_' + tabela

    # executa a query
    query = f'SELECT {idcon} FROM {tabela} WHERE {idcon} = (SELECT MAX({idcon}) FROM {tabela})'
    cursor.execute(query)
    select = cursor.fetchall()

    if select:
        df_select = pd.DataFrame(select)
        index = df_select.iloc[0][0]
    else:
        index=0
    
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return index

def select_nome_descricao(query):

     # abre a conexão com o banco
    conn, cursor = connect()

    # executa a query
    cursor.execute(query)
    select = cursor.fetchall()

    # transforma o resultado em um dataframe
    df_select = pd.DataFrame(select)
    
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_select

# faz a conexão com o banco
def connect():
    
    # define a string de conexão
    conn = psycopg2.connect(
        database = 'cheer',
        user = 'postgres',
        password = 'dabdog',
        host = 'localhost',
        port = '5432'
    )

    # cria um cursor pra executar as querys
    cursor = conn.cursor()

    return conn, cursor

# fecha a conexão com o banco
def disconnect(conn, cursor):
    cursor.close()
    conn.close()