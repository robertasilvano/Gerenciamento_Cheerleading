import psycopg2
import pandas as pd

# seleciona as colunas da tabela escolhida
def get_column_names(tabela):

    # abre a conexão com o banco
    conn, cursor = connect()

    # define a query para selecionar os nomes das colunas
    query = f'SELECT column_name, data_type FROM information_schema.columns WHERE TABLE_NAME = \'{tabela}\''

    # executa a query
    cursor.execute(query)
    colunas = cursor.fetchall()

    # transforma o resultado em um dataframe 
    df_colunas = pd.DataFrame(colunas, columns=['Coluna', 'Tipo de dado'])
        
    # fecha a conexão com o banco
    disconnect(conn, cursor)

    return df_colunas

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