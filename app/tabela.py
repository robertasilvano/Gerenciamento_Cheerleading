def escolher_tabela():

    tabela_dict = {

        1: 'alergia',
        2: 'atleta',
        3: 'atleta_alergia',
        4: 'atleta_evento_posicao',
        5: 'atleta_fluxocaixa',
        6: 'atleta_medicamento',
        7: 'atleta_posicao',
        8: 'atleta_skill',
        9: 'contato_Emergencia',
        10: 'diretoria',
        11: 'diretoria_projeto',
        12: 'doenca',
        13: 'doenca_atleta',
        14: 'efeito_Colateral',
        15: 'evento',
        16: 'evento_fluxocaixa',
        17: 'falta',
        18: 'fluxo_Caixa',
        19: 'medicamento',
        20: 'medicamento_efeitocolateral',
        21: 'posicao',
        22: 'projeto',
        23: 'skill'
    }

    print('OPÇÕES DE TABELA: ')
    
    for tabela in tabela_dict:
        print(f'[{tabela}] - {tabela_dict[tabela]}')

    tabela_escolhida = int(input('\nEscolha a tabela desejada: '))

    if tabela_escolhida < 1 or tabela_escolhida > 23:
        print('Você escolheu um valor inválido. Escolha novamente: ')
        escolher_tabela()

    print(f'Você escolheu a tabela [{tabela_escolhida}] - {tabela_dict[tabela_escolhida]}\n')

    return tabela_dict[tabela_escolhida]
