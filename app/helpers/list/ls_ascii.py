import os

from flask import current_app


def ls_ascii_in_group(group_path: str) -> list[str]:

    """Retorna todos os ascii no grupo solicitado"""


    # path para os arquivos ascii
    folder_path: str = current_app.config['ASCII_FOLDER']

    try:
        return os.listdir(f'{folder_path}/{group_path}')
    except FileNotFoundError:
        return False


def ls_ascii_groups() -> list[str]:

    """Retorna todos os grupos de ascii no path definido para ser a pasta para os ascii"""


    # path para os arquivos ascii
    folder_path: str = current_app.config['ASCII_FOLDER']

    return os.listdir(folder_path)


def ls_all_ascii() -> dict[list[str]]:

    """Retorna um dict contendo todos os ascii em seus respectivos grupos. ex: {'grupo1': [<todos_os_ascii_do_grupo1>]}"""


    # path para os arquivos ascii
    folder_path: str = current_app.config['ASCII_FOLDER']


    # Listagem de todos os grupos ascii
    all_ascii_groups: list[str] = ls_ascii_groups()

    # Dicionario contendo todos os grupos e todos os ascii dentro deles
    all_ascii_dict: dict[list[str]] = {}

    for group in all_ascii_groups:
        all_ascii_dict[group] = ls_ascii_in_group(group)

    return all_ascii_dict
    


# def ls_routes():
#     pass


# def ls_ascii(specific_group=None, return_only_groups=True):

    
#     # Caminho para onde estão armazenados os ascii
#     folder_path: str = current_app.config['ASCII_FOLDER']


#     # Se a busca for por os ascii de um grupo especifico
#     if specific_group is not None:

#         try:
#             return os.listdir(f'{folder_path}/{specific_group}')
        
#         except FileNotFoundError:
#             return False



#     # Todos os grupos de artes ascii
#     ascii_groups: list[str] = os.listdir(f'{folder_path}/')

#     # Se for requisitado apenas os grupos de artes, e não todas as artes...
#     if return_only_groups is True:

#         return ascii_groups
    

#     # Array para passar com o array os nomes do grupos no [n][0], 
#     # e no [n][1] todas a listas de artes ascii respectivas
#     for i in range(len(ascii_groups)):

#         ascii_groups[i] = ascii_groups[i], os.listdir(f'{folder_path}/{ascii_groups[i]}')

#     return ascii_groups
