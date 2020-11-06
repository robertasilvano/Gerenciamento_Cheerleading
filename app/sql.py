import psycopg2
import pandas as pd

def select_colunas(tabela):
    conn, cursor = connect()

    query = f'SELECT column_name, data_type FROM information_schema.columns WHERE TABLE_NAME = \'{tabela}\''
    
    print('QUERY: ' + query + '\n')

    cursor.execute(query)
    colunas = cursor.fetchall()
    df_colunas = pd.DataFrame(colunas, columns=['Coluna', 'Tipo de dado'])
        
    disconnect(conn, cursor)

    return df_colunas

def select_query(query, col_selecionadas_vetor):

    conn, cursor = connect()

    cursor.execute(query)

    select = cursor.fetchall()
    df_select = pd.DataFrame(select, columns = col_selecionadas_vetor)
        
    disconnect(conn, cursor)

    return df_select

def connect():
    
    conn = psycopg2.connect(
        database = 'cheer',
        user = 'postgres',
        password = 'dabdog',
        host = 'localhost',
        port = '5432'
    )

    cursor = conn.cursor()

    return conn, cursor

def disconnect(conn, cursor):
    cursor.close()
    conn.close()