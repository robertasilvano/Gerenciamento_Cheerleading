from escolher_colunas import escolher_colunas
from acao import acao_select, acao_insert, acao_update, acao_delete

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
        5: 'SAIR'
    }
    
    # cria o menu das opções de ações disponíveis
    print('OPÇÕES DE AÇÕES: ')
    for acao in acao_dict:
        print(f'[{acao}] - {acao_dict[acao]}')

    acao_escolhida = int(input('\nEscolha a ação desejada: '))

    if acao_escolhida < 1 or acao_escolhida > 5:
        print(f'\n{bold_underline}Opção inválida! Escolha novamente.{end_bold_underline}')
        return 'Play'

     # verifica qual ação foi escolhida e chama a função da mesma
    print(f'Você escolheu a opção {bold_underline}[{acao_escolhida}] - {acao_dict[acao_escolhida]}{end_bold_underline}')
    if acao_escolhida == 1:
        colunas = escolher_colunas(tabela)
        acao_select(tabela, colunas)

    elif acao_escolhida == 2:
        colunas = escolher_colunas(tabela)
        acao_insert(tabela, colunas)

    elif acao_escolhida == 3:
        colunas = escolher_colunas(tabela)
        acao_update(tabela, colunas)

    elif acao_escolhida == 4:
        acao_delete(tabela)

    elif acao_escolhida == 5:
        print(f'Você escolheu [{acao_escolhida}] - Sair')
        print('Encerrando o programa')
        exit()
