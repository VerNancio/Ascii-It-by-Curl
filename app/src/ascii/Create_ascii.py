import os
import ascii.convert
import regex as re

# from pywhatkit.ascii_art import image_to_ascii_art
import ascii

from .Ascii import Ascii


class Create_ascii(Ascii):


    def __init__(self, ascii_width: int=80) -> None:
        super().__init__()

        self.ascii_width = ascii_width 

    
    def set_ascii_width(self, ascii_width) -> None: self.ascii_width = ascii_width


    def frames_to_ascii(frames_path: str, output_folder: str="def", ascii_width: int=80):

        # # Loop através de todos os arquivos na pasta
        # for filename in os.listdir(f"{frames_path}/{output_folder}"):

        #     # Verifica se o caminho é um arquivo (e não uma subpasta)
        #     if os.path.isfile(os.path.join(f"{frames_path}/{output_folder}", filename)):

        #         # Faça algo com o arquivo
        #         print(filename)


        # Listagem de todos os arquivos no diretório indicato
        folder_files = os.listdir(frames_path)

        frames_files = [filename for filename in folder_files if re.match(pattern=r"^frame_\d+\.jpg$", string=filename)] 


        frames_dict: dict[str] = {}

        for f in frames_files:

            file_number = f[f.rindex("_") + 1:f.rindex(".")]

            frames_dict[file_number] = f


        # Cria o output_folder se ele não existir
        if not os.path.exists("files/ascii_folder"):
            os.makedirs("files/ascii_folder")

        # Cria o output_folder se ele não existir
        if not os.path.exists(f"{output_folder}"):
            os.makedirs(f"{output_folder}")


        for i in range(len(frames_dict)):

            img_path: str = f"frames_folder/{output_folder}/{frames_dict[str(i)]}"
            output_file: str = f"ascii_folder/{output_folder}/ascii_{str(i)}"

            img = ascii.color

            # image_to_ascii_art(img_path=img_path, output_file=output_file, ascii_width=ascii_width)


        print(frames_dict)


    @staticmethod
    def create_by_folder(self) -> None:

        
        # folder_path: str = filedialog.askdirectory(initialdir="C:/", title="Select a directory")

        files: list[str] = os.listdir(folder_path)


        # Nome do diretorio final onde todos os ascii vao ficar juntos
        output_folder_name: str = input("Qual o nome da pasta onde ficarão os ascii? ")


        # Checa se a extensão do arquivo é tida como válida para conversão do video; ex: "mp4"
        check_extension: str = lambda f, val_ext: f[f.rindex(".") + 1:] in val_ext

        valid_videos_files: list[str] = [file for file in files if check_extension(file, self.valid_extension)]


        for file in valid_videos_files:

            abs_path: str = os.path.join(folder_path, file)
            output_folder_path: str = os.path.join(output_folder_name, file)

            create_ascii(abs_path, output_folder_path)


    @staticmethod
    def create_ascii(files_folder_path:str, file_path: str = None, output_folder: str = None) -> None:

        # if file_path is None:
        #     file_path: str = filedialog.askopenfilename(initialdir="C:/", title="Select a File")

        # if output_folder is None:
        #     output_folder: str = input("Qual o nome da pasta? ")


        ascii_width = 400

        print(file_path, '--- ', output_folder)

        video_to_frames(file_path=file_path, output_folder=output_folder)
        # frames_to_ascii(frames_path=output_folder, output_folder=output_folder, ascii_width=ascii_width)

