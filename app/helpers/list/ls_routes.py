import os

from flask import current_app


def ls_base_routes() -> list[str]:

    """
    Retorna todas as rotas base \n 
    ex: 'list', 'stream', 'upload'
    """

    # Dicionario contendo todas as rotas e subrotas
    routes_dict: dict[dict[list[str]]] = current_app.config['ALL_ROUTES_DICT']


    # Chaves do dicionario interno (o nome das rotas base)
    base_routes: list[str] = routes_dict.keys()

    return base_routes



def ls_sub_routes() -> dict[list[str]]:

    """
    Retorna um dicionario com todas as rotas principais e suas subrotas
    """

    # Dicionario contendo todas as rotas e subrotas
    routes_dict: dict[dict[list[str]]] = current_app.config['ALL_ROUTES_DICT']

    
    # Chaves do dicionario interno (o nome das rotas base)
    base_routes: list[str] = routes_dict.keys()

    # Dicionario já contendo todas as rotas base como keys de uma lista vazia
    sub_route_dict: dict[list[str]] = {route: [] for route in base_routes}

    for route in base_routes:

        for sub_route in routes_dict[route].keys():

            sub_route_dict[route] += [sub_route]

    return sub_route_dict


def ls_specific_sub_routes(specific_route: str):

    # Dicionario contendo todas as rotas e subrotas
    routes_dict: dict[dict[list[str]]] = current_app.config['ALL_ROUTES_DICT']


    specific_subroutes_list: list[str] = []

    for base_route in routes_dict:

        for sub_route in base_route:

            if base_route == specific_route: 
                specific_subroutes_list = routes_dict[base_route].keys()

            elif sub_route == specific_route: 
                specific_subroutes_list = routes_dict[base_route][sub_route]

    return specific_subroutes_list
