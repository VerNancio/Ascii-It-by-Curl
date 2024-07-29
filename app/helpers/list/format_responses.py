# #
# # FORMATACAO DAS ROTAS E DOS ASCII
# #



# 
# #    ASCII
# 


def format_ascii_groups_response(ascii_groups: list[str]) -> str:

    """Retorna uma resposta já nos moldes de ser impressa de todos os grupos de ascii"""


    formated_str = '\nGrupos disponíveis: \n\n'

    for group_name in ascii_groups:
        formated_str += f' - {group_name}\n'

    return formated_str + '\n'


def format_ascii_in_group_response(group_name: str, ascii_list: list[str]) -> str:

    """Retorna uma resposta já nos moldes de ser impressa de todos os ascii dentro de grupos"""


    formated_str = f'\nASCIIs no grupo "{group_name}": \n\n'

    for ascii_name in ascii_list:
        formated_str += f' - {ascii_name}\n'

    return formated_str + '\n'



def format_all_ascii_response(all_ascii_dict: dict[list[str]]) -> str:

    """Retorna uma resposta já nos moldes de ser impressa de todos os grupos e seus subsequentes ascii"""


    formated_str = '\nGrupos e artes ascii disponíveis para stream: \n\n'

    for group_name, ascii_list in all_ascii_dict.items():

        formated_str += f'  /{group_name}\n'

        for ascii_name in ascii_list:
            formated_str += f'    /{ascii_name}\n'

        formated_str += '\n'

    return formated_str + '\n'



# 
# # Routes
# 


def format_base_routes_response(base_routes: list[str]) -> str:

    """Retorna uma resposta já nos moldes de ser impressa de todos os grupos e seus subsequentes ascii"""


    formated_str = '\nRotas disponíveis: \n\n'

    for route in base_routes:
        formated_str += f'  /{route}\n'

    return formated_str + '\n'


def format_sub_routes_response(sub_routes_dict: dict[list[str]]) -> str:

    """Retorna uma resposta já nos moldes de ser impressa de todos os grupos e seus subsequentes ascii"""


    formated_str = '\nRotas e subrotas disponíveis: \n\n'

    for base_route, sub_routes in sub_routes_dict.items():

        formated_str += f'  /{base_route}\n'

        for route in sub_routes:
            formated_str += f'     /{route}\n'

        # formated_str += '\n'

    return formated_str + '\n'


def format_specific_sub_routes_response(specific_route: str, sub_routes: list[str]) -> str:

    """Retorna uma resposta já nos moldes de ser impressa de todas as subrotas de uma rota"""


    if len(sub_routes) == 0: return '\nNão existem subrotas da rota visada.\n'
    

    formated_str = f'\nSubrotas de {specific_route}: \n\n'

    for route in sub_routes:

        formated_str += f'  /{route}\n'

    return formated_str + '\n'



    