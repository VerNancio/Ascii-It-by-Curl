import os
import ascii.convert
import regex as re

import ascii


def frames_to_ascii(frames_path: str, output_folder: str="def", ascii_width: int=80):

    # Listagem de todos os arquivos no diretório indicato
    folder_files = os.listdir(frames_path)

    frames_files = [filename for filename in folder_files if re.match(pattern=r"^frame_\d+\.jpg$", string=filename)] 


    frames_dict = {}

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


    # print(frames_dict)
