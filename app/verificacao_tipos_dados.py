from sql import get_column_datatypes
import pandas as pd

def verificacao_tipos_dados(tabela, col_selecionadas_vetor, values):
    # pega o tipo das colunas, cria o menu, e pega o input
    df_datatype = get_column_datatypes(tabela)

    for index, row in df_datatype.iterrows():
        print(index)
        if (row['Coluna']) not in col_selecionadas_vetor:
            df_datatype.drop(index, inplace=True)

    for index, row in df_datatype.iterrows():
        print(type(values[index]))
        if row['Tipo'] == type(values[index]):
            print(values[index])