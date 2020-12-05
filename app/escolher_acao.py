from escolher_colunas import escolher_colunas, colunas_all
from acao import acao_select, acao_insert, acao_update, acao_delete, acao_espec

# cria um menu para o usuário escolher a ação a ser executada sobre a tabela escolhida
def escolher_acao(tabela):

    bold_underline = '\033[1m \033[4m'
    end_bold_underline = '\033[0m'

    # cria um dicionário das ações possíveis
    acao_dict = {
        1: 'SELECT',
        2: 'INSERT',
        3: 'UPDATE',
        4: 'DELETE',
        5: 'CONSULTA ESPECÍFICA 1: Quantos atletas existem em cada posição',
        6: 'CONSULTA ESPECÍFICA 2: Quantidade de projetos que cada diretoria tem',
        7: 'CONSULTA ESPECÍFICA 3: Média da mensalidade de cada atleta que possua média maior que R$20.00',
        8: 'SAIR',
        9: 'RETORNAR AO MENU DE TABELAS'
    }
    
    # cria o menu das opções de ações disponíveis
    print('OPÇÕES DE AÇÕES: ')
    for acao in acao_dict:
        print(f'[{acao}] - {acao_dict[acao]}')

    acao_escolhida = int(input('\nEscolha a ação desejada: '))

    # retorna ao menu de tabelas
    if acao_escolhida == 9:
        return 'Tabelas'

    # executa de novo o menu de ações
    elif acao_escolhida < 1 or acao_escolhida > 9:
        print(f'\n{bold_underline}Opção inválida! Escolha novamente.{end_bold_underline}')
        return 'Play'

     # verifica qual ação foi escolhida e chama a função da mesma
    print(f'Você escolheu a opção {bold_underline}[{acao_escolhida}] - {acao_dict[acao_escolhida]}{end_bold_underline}')

    # SE A AÇÃO FOR:
    # select ou update: é necessário escolher sobre quais colunas vai querer executar a ação, e depois chama a ação
    # insert: é necessário dar insert em todas as colunas, visto que todas são not null. então seleciona todas as colunas, e depois chama a ação
    # delete:  não é necessário escolher colunas, então chama a ação
    # consulta específica: define as querys e chama a ação
    if acao_escolhida == 1:
        colunas, flag = escolher_colunas(tabela)

        if flag == 'Tabelas':
            return 'Tabelas'
        elif flag == 'Ações':
            return 'Play'

        acao_select(tabela, colunas)
        return 'Tabelas'

    elif acao_escolhida == 2:
        colunas = colunas_all(tabela)
        acao_insert(tabela, colunas)
        return 'Tabelas'

    elif acao_escolhida == 3:
        colunas, flag = escolher_colunas(tabela)

        if flag == 'Tabelas':
            return 'Tabelas'
        elif flag == 'Ações':
            return 'Play'
            
        acao_update(tabela, colunas)
        return 'Tabelas'

    elif acao_escolhida == 4:
        acao_delete(tabela)
        return 'Tabelas'

    elif acao_escolhida == 5:
        query = '''
        SELECT p.descricao AS posicao, count(a.id_atleta) AS qtd_atleta,
        string_agg(a.nome, ', ') AS atletas FROM atleta_posicao AS ap
        LEFT JOIN atleta AS a ON a.id_atleta = ap.id_atleta
        LEFT JOIN posicao AS p ON p.id_posicao = ap.id_posicao
        GROUP BY p.descricao
        ORDER BY p.descricao;
        '''
        colunas = ['posição', 'qtd_atleta', 'atletas']
        acao_espec(query, colunas)
        return 'Tabelas'
        
    elif acao_escolhida == 6:
        query = '''
        SELECT d.descricao AS diretoria, count(p.id_projeto) AS qtd_projeto,
        string_agg(p.descricao, ', ') AS projetos FROM diretoria AS d
        LEFT JOIN diretoria_projeto AS dp ON dp.id_diretoria = d.id_diretoria
        LEFT JOIN projeto AS p ON p.id_projeto = dp.id_projeto
        GROUP BY d.descricao
        ORDER BY d.descricao;
        '''
        colunas = ['diretoria', 'qtd_projeto', 'projetos']
        acao_espec(query, colunas)
        return 'Tabelas'

    elif acao_escolhida == 7:
        query = '''
        SELECT a.nome, avg(fc.valor) AS media_mensalidade FROM atleta AS a
        LEFT JOIN atleta_fluxo_caixa AS afc ON afc.id_atleta = a.id_atleta
        LEFT JOIN fluxo_caixa AS fc ON fc.id_fluxo_caixa = afc.id_fluxo_caixa
        WHERE fc.descricao = 'mensalidade'
        GROUP BY a.nome
        HAVING avg(fc.valor) > 20 ORDER BY a.nome;
        '''
        colunas = ['nome', 'media_mensalidade']
        acao_espec(query, colunas)
        return 'Tabelas'

    elif acao_escolhida == 8:
        print('Encerrando o programa')
        exit()
