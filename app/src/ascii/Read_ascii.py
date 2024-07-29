import os

from .Ascii import Ascii

from ...helpers.list.ls_ascii import *


class Read_ascii(Ascii):


    def __init__(self) -> None:
        super().__init__()

    
    def read_ascii(self, ascii_target) -> list[str]:

        # Caminho para a ser retornado
        ascii_path = f"{self.ascii_folder}/{ascii_target}"

        # Puxar todos arquivos com ascii do vídeo exigido
        ascii_files: list[str] = os.listdir(ascii_path)


        # Dicionário para a aparição dos ascii em ordem
        ascii_dict = {}

        for f in ascii_files:

            # Utiliza o seu numero de registro antes do começo da extensão, ex: ascii_10.txt -> 10
            file_number: str = f[f.rindex("_") + 1: f.rindex(".")]
            ascii_dict[file_number] = f


        ascii_frames: list[str] = []

        for i in range(len(ascii_dict)):

            file_to_open: str = ascii_dict[str(i)]

            with open(f"{self.ascii_folder}/{ascii_target}/{file_to_open}") as f:

                ascii_frame: str = f.read()

                ascii_frames.append(ascii_frame)

        return ascii_frames


    def read_group(self, ascii_group_target) -> list[list[str]]:

        # Caminho para o grupo de arquivos a ser retornados
        ascii_group_path = f"{self.ascii_folder}/{ascii_group_target}"

        # Listagem de pastas das artes asciis
        ascii_names: list[str] = os.listdir(ascii_group_path)
        print(ascii_names)


        # Lista a ser retornada com as artes ascii 
        ascii_list:list[str][str] = []

        for ascii_name in ascii_names:

            # Caminho de um ascii especifico dentro do grupo
            ascii_target = f"{ascii_group_target}/{ascii_name}"

            # Frames das artes ascii
            ascii_frames = self.read_ascii(ascii_target)

            ascii_list.append(ascii_frames)

        return ascii_list
    

    def read_random():

        pass

    
    # def 