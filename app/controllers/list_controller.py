from flask import Blueprint, request, current_app


from ..helpers.list.ls_ascii import *
from ..helpers.list.ls_routes import *

from ..helpers.check.check_ascii import *
from ..helpers.check.check_routes import *

from ..helpers.list.format_responses import *


bp = Blueprint('list', __name__, url_prefix='/')

PATH_PREFIX = 'list'


@bp.route("/")
@bp.route(f'{PATH_PREFIX}')
def ls():

    # ls_base_routes()
    # ls_sub_routes()

    # return format_routes_response(ls_base_routes())
    # return format_sub_routes_response(ls_sub_routes())

    # Verificador se requisição é via curl
    if 'curl' not in request.user_agent.string:
        return 'Aplicação só disponível via curl :X'


    res: str = ''

    # Adiciona a resposta de todas as rotas principais e suas subrotas
    sub_routes_dict: dict[list[str]] = ls_sub_routes()
    res += format_sub_routes_response(sub_routes_dict=sub_routes_dict)

    # Adiciona a resposta todos os grupos de ascii
    ascii_groups: list[str] = ls_ascii_groups()
    res += format_ascii_groups_response(ascii_groups=ascii_groups)
    
    return res


@bp.route(f'{PATH_PREFIX}/<specific_info>')
def specific_list(specific_info: str):

    specific_info = specific_info.lower()


    res: str

    valid_sub_routes = current_app.config['ALL_ROUTES_DICT']


    if specific_info in valid_sub_routes['list']['groups']:
        ascii_groups: list[str] = ls_ascii_groups()

        res = format_ascii_groups_response(ascii_groups=ascii_groups)

    elif specific_info in valid_sub_routes['list']['all_ascii']:
        all_ascii_dict: dict[list[str]] = ls_all_ascii()

        res = format_all_ascii_response(all_ascii_dict=all_ascii_dict)
    
    elif specific_info in valid_sub_routes['list']['routes']:
        sub_routes_dict: dict[list[str]] = ls_sub_routes()

        res = format_sub_routes_response(sub_routes_dict=sub_routes_dict)

    elif specific_info in valid_sub_routes['list']['allowed_extensions']:

        res = 'saas'

    else: 
        app_domain = request.host.split(':')[0]
        app_port = request.host.split(':')[1]

        res = f"""\nRota não existente.\n\nPara saber quais rotas e subrotas existem use a rota: \"{app_domain}:{app_port}/list/routes\"\n"""

    return res


@bp.route(f'{PATH_PREFIX}/<sub_route_info>/<specific_info>')
def list_group_ascii(sub_route_info: str, specific_info: str):

    sub_route_info = sub_route_info.lower()
    specific_info = specific_info.lower()


    # Resposta a ser retornada
    res: str

    valid_sub_routes = current_app.config['ALL_ROUTES_DICT']

    if sub_route_info in valid_sub_routes['list']['groups']:

        ascii_groups: list[str] = ls_ascii_groups()

        if specific_info in ascii_groups:
            ascii_list: list[str] = ls_ascii_in_group(group_path=specific_info)

            res = format_ascii_in_group_response(group_name=specific_info, ascii_list=ascii_list)
            
        else:
            res = '\nGrupo ascii solicitado não existe\n'
            res += format_ascii_groups_response(ascii_groups)

    elif sub_route_info in valid_sub_routes['list']['routes']:

        # Rota especifica visada
        specific_route: str = specific_info

        # Subrotas da rota procurada
        sub_routes: list[str] = ls_specific_sub_routes(specific_route=specific_route)

        res = format_specific_sub_routes_response(specific_route=specific_route, sub_routes=sub_routes)

    else:
        app_domain = request.host.split(':')[0]
        app_port = request.host.split(':')[1]

        res = f"""\nRota não existente.\n\nPara saber quais rotas e subrotas existem use a rota: \"{app_domain}:{app_port}/list/routes\"\n"""

    return res
