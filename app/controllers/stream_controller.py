from flask import Blueprint, request, Response
from time import sleep

from ..helpers.list.ls_ascii import *
from ..helpers.list.format_responses import *

from ..src.ascii.Ascii import Ascii

from ..src.ascii.Read_ascii import Read_ascii
from ..src.ascii.Run_ascii import Run_ascii

from ..helpers.check.check_ascii import ascii_exists


bp = Blueprint('stream', __name__, url_prefix='/')

PATH_PREFIX = 'stream'


def stream(ascii_to_stream: list[str], max_loops: int = 3, color: str = None, stream_mode: str = 'random'):

    if stream_mode in ['single', 'random']:
        for ascii_str in Run_ascii().run_ascii(ascii_to_stream): 

            sleep(0.06)
            yield ascii_str

    else:
        for ascii_str in Run_ascii().run_ascii_group(ascii_to_stream, max_loops=max_loops):

            sleep(0.06)
            yield ascii_str        



# STREAM PREFIX

@bp.route(f'{PATH_PREFIX}')
def st_prefix():
    
    # Argumentos passados via GET
    args = request.form

    # Quantidade de loops para cada arte ascii (Padrão é 3)
    loops: int = 3 if not args.get('loops') else int(args.get('loops'))

    
    # Pega uma arte ascii aleatória para stream
    ascii_path = Ascii().get_random_ascii_path()

    # Retorna o ascii alvo para stream
    ascii_to_stream: list[str] = Read_ascii().read_ascii(ascii_path)

    return Response(stream(ascii_to_stream=ascii_to_stream), mimetype='text/plain')


@bp.route(f'{PATH_PREFIX}/<stream_mode>')
def st_mode(stream_mode):

    # Argumentos passados via GET
    args = request.form

    # Quantidade de loops para cada arte ascii (Padrão é 3)
    loops: int = 3 if not args.get('loops') else int(args.get('loops'))


    if stream_mode in ['single', 'random']:
        
        # Pega uma arte ascii aleatória para stream
        ascii_path = Ascii().get_random_ascii_path()

        # Retorna o ascii alvo para stream
        ascii_to_stream: list[str] = Read_ascii().read_ascii(ascii_path)

    elif stream_mode == 'group':

        # Pega um grupo ascii aleatório para stream
        ascii_group = Ascii().get_random_ascii_group()

        # Retorna o ascii alvo para stream
        ascii_to_stream: list[str] = Read_ascii().read_group(ascii_group)

    return Response(stream(ascii_to_stream=ascii_to_stream, stream_mode=stream_mode), mimetype='text/plain')


@bp.route(f'{PATH_PREFIX}/<stream_mode>/<path_arg_1>')
def st_one_param(stream_mode, path_arg_1):

    # Argumentos passados via GET
    args = request.form

    # Quantidade de loops para cada arte ascii (Padrão é 3)
    loops: int = 3 if not args.get('loops') else int(args.get('loops'))


    if stream_mode == 'single':

        # Nome da arte ascii
        ascii_name = path_arg_1

        # Nome do grupo ascii onde esta
        ascii_group = ascii_exists(ascii_name)[0]

        ascii_path = f'{ascii_group}/{ascii_name}'

        # Retorna o ascii alvo para stream
        ascii_to_stream: list[str] = Read_ascii().read_ascii(ascii_path)

    elif stream_mode == 'group':

        # Nome do grupo ascii
        ascii_group = path_arg_1

        # Retorna o ascii alvo para stream
        ascii_to_stream: list[str] = Read_ascii().read_group(ascii_path)
    
    return Response(stream(ascii_to_stream=ascii_to_stream, stream_mode=stream_mode), mimetype='text/plain')


@bp.route(f'{PATH_PREFIX}/<stream_mode>/<path_arg_1>/<path_arg_2>')
def st_two_param(stream_mode, path_arg_1, path_arg_2):

    if stream_mode != 'single':
        return "Path com 4 parametros inválido senão para single"

    # Argumentos passados via GET
    args = request.form

    # Quantidade de loops para cada arte ascii (Padrão é 3)
    loops: int = 3 if not args.get('loops') else int(args.get('loops'))


    ascii_path = f'{path_arg_1}/{path_arg_2}'

    # Retorna o ascii alvo para stream
    ascii_to_stream: list[str] = Read_ascii().read_ascii(ascii_path)

    return Response(stream(ascii_to_stream=ascii_to_stream, stream_mode=stream_mode), mimetype='text/plain')
