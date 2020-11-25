import psycopg2
import pandas as pd

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

# retorna o nome de todas as tabelas
def get_table_names():

    # abre a conexão com o banco
    conn, cursor = connect()

    query = 'SELECT table_name FROM information_schema.tables WHERE table_schema=\'public\' AND table_type=\'BASE TABLE\';'

    # executa a query
    cursor.execute(query)
    tabelas = cursor.fetchall()

    # transforma o resultado em um dataframe 
    df_tabelas = pd.DataFrame(tabelas, columns=['Tabela']).sort_values('Tabela').reset_index(drop=True)
    df_tabelas.index = df_tabelas.index + 1
        
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_tabelas

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

# faz o select da tabela e colunas desejadas
def select(query, colunas):

    # abre a conexão com o banco
    conn, cursor = connect()

    # executa a query
    cursor.execute(query)
    select = cursor.fetchall()

    # transforma o resultado em um dataframe
    df_select = pd.DataFrame(select, columns=colunas)
    df_select.columns = df_select.columns.str.upper()
    
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_select
