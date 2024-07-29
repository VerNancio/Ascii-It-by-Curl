import os
import random
# import sys
# from time import sleep


import ascii

from ...helpers.list.ls_ascii import *



class Ascii:


    def __init__(self, base_path = None, ascii_folder = None, frames_folder = None) -> None:

        self.valid_extension: list[str] = ["mp4"]

        # Se o caminho base nao for nulo, altera o caminho
        self.base_path = base_path if base_path is not None else os.getcwd()

        # Se o caminho dos ascii nao for nulo, altera o caminho
        self.ascii_folder = ascii_folder if ascii_folder is not None else f'files/ascii_folder'

        # Se o caminho dos arquivos nao for nulo, altera o caminho
        self.frames_folder = frames_folder if frames_folder is not None else f'files/frames_folder'



    @staticmethod
    def get_random_ascii_path() -> str:

        """Retorna o caminho de uma arte ascii aleatória"""

        # Pega um grupo aleatório
        ascii_group_name: str = Ascii.get_random_ascii_group()

        # Retorna todos as artes ascii dentro do grupo
        ascii_list: list[str] = ls_ascii_in_group(ascii_group_name)

        ascii_name = ascii_list[random.randint(0, len(ascii_list) - 1)]

        ascii_path = f'{ascii_group_name}/{ascii_name}'

        return ascii_path


    @staticmethod
    def get_random_ascii_group() -> str:
        """Retorna o nome de um grupo ascii aleatório"""

        ascii_groups = ls_ascii_groups()

        return ascii_groups[random.randint(0, len(ascii_groups) - 1)]
        


    # # Se o caminho base nao for nulo, altera o caminho
    # def set_base_path(self, base_path):
    #     self.base_path = base_path if base_path is not None else self.base_path

    # # Se o caminho dos ascii nao for nulo, altera o caminho
    # def set_ascii_folder(self, ascii_folder):
    #     self.ascii_folder = ascii_folder if ascii_folder is not None else self.ascii_folder

    # # Se o caminho dos arquivos nao for nulo, altera o caminho
    # def set_frames_folder(self, frames_folder):
    #     self.frames_folder = frames_folder if frames_folder is not None else self.frames_folder

    
    # def run_ascii_group(self, target_folder, max_loops):

    #     # Listagem de pastas das artes asciis
    #     ascii_groups: list[str] = os.listdir("files/ascii_folder")
        

    #     if target_folder in ascii_groups:

    #         inner_folders: list[str] = os.listdir(f"files/ascii_folder/{target_folder}")

    #         while True:

    #             for ascii_folder in inner_folders:

    #                 ascii_folder = f"{target_folder}/{ascii_folder}"

    #                 for ascii in self.run_ascii(ascii_folder=ascii_folder, max_loops=max_loops):

    #                     yield ascii


    # @staticmethod
    # def run_ascii(ascii_folder = None, max_loops = -1, color = colorama.Fore.LIGHTRED_EX):


    #     if ascii_folder == None:

    #         ascii_group: str = input("Qual o nome da pasta? ")
    #         ascii_folder: str = input("Qual o nome da imagem? ")

    #         ascii_folder = f"{ascii_group}/{ascii_folder}"

    #     # Puxar todos arquivos com ascii do vídeo exigido
    #     ascii_files: list[str] = os.listdir(f"files/ascii_folder/{ascii_folder}")


    #     # Dicionário para a aparição dos ascii em ordem
    #     ascii_dict = {}

    #     for f in ascii_files:

    #         # Utiliza o seu numero de registro antes do começo da extensão
    #         file_number: str = f[f.rindex("_") + 1: f.rindex(".")]
    #         ascii_dict[file_number] = f


    #     loop_count = 0

    #     while True:

    #         loop_count += 1

    #         for i in range(len(ascii_dict)):

    #             file_to_open: str = ascii_dict[str(i)]

    #             with open(f"files/ascii_folder/{ascii_folder}/{file_to_open}") as f:

    #                 ascii_frame: str = f.read()

    #                 yield color + f"\033[2J\033[1;1f{ascii_frame}"

    #                 sleep(0.01)


    #         if loop_count == max_loops: 
    #             break


    # @staticmethod
    # def create_by_folder(self) -> None:

        
    #     # folder_path: str = filedialog.askdirectory(initialdir="C:/", title="Select a directory")

    #     files: list[str] = os.listdir(folder_path)


    #     # Nome do diretorio final onde todos os ascii vao ficar juntos
    #     output_folder_name: str = input("Qual o nome da pasta onde ficarão os ascii? ")


    #     # Checa se a extensão do arquivo é tida como válida para conversão do video; ex: "mp4"
    #     check_extension: str = lambda f, val_ext: f[f.rindex(".") + 1:] in val_ext

    #     valid_videos_files: list[str] = [file for file in files if check_extension(file, self.valid_extension)]


    #     for file in valid_videos_files:

    #         abs_path: str = os.path.join(folder_path, file)
    #         output_folder_path: str = os.path.join(output_folder_name, file)

    #         create_ascii(abs_path, output_folder_path)

    # @staticmethod
    # def create_ascii(files_folder_path:str, frames_folder: str = None, output_folder: str = None) -> None:

    #     # if frames_folder is None:
    #     #     frames_folder: str = filedialog.askopenfilename(initialdir="C:/", title="Select a File")

    #     # if output_folder is None:
    #     #     output_folder: str = input("Qual o nome da pasta? ")


    #     ascii_width = 400

    #     print(frames_folder, '--- ', output_folder)

    #     video_to_frames(frames_folder=frames_folder, output_folder=output_folder)
    #     # frames_to_ascii(frames_folder=output_folder, output_folder=output_folder, ascii_width=ascii_width)
