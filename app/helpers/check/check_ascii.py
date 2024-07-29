from flask import current_app

from ..list.ls_ascii import ls_all_ascii, ls_ascii_groups


def ascii_exists(ascii_name: str) -> list[str]:

    """Verifica se um determinado arquivo existe """
    
    
    # path para os arquivos ascii
    folder_path: str = current_app.config['ASCII_FOLDER']


    # Dicionario contendo todos os grupos e todos os ascii dentro deles
    all_ascii_dict: dict[list[str]] = ls_all_ascii()

    # Lista para retornar todos os grupos que possuem o ascii com nome correspondente
    ascii_exists_ls: list[str] = []

    for group_name, group_ascii in all_ascii_dict.items():

        for ascii in group_ascii:
            if ascii_name == ascii: ascii_exists_ls.append(group_name)

    return ascii_exists_ls


def ascii_group_exists(group_name: str):

    """Checa se determinado grupo de ascii existe"""
    
    
    ascii_groups: list[str] = ls_ascii_groups()

    return group_name in ascii_groups