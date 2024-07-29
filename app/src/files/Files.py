from flask import Flask, Response, request 

from werkzeug.utils import secure_filename


class Files:

    self.valid_extension = list[str] = ["mp4"]
    self.path_to_save = '..'


    def __init__(self, files) -> None:
        
        self.files = files


    def allowed_file(filename: str):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.valid_extension

    def save():


        # Permitido se for True e ter extensão permitida
        allowed_files = [file for file in self.files if file and self.allowed_file(file.filename)]


        # if file and self.allowed_file(file.filename):

        # group = 'group'

        for file in allowed_files:

            file.filename = secure_filename(file.filename)
            file.save()



            # file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # output_path = os.path.join(app.config['ASCII_FOLDER'], filename)

            # Salva o arquivo no determinado diretório 
            # print('---->', app.config['UPLOAD_FOLDER'])

        # Ascii_manipulation().create_ascii(files_folder_path=app.config['FILES_FOLDER'], 
        #                                   file_path=file_path, 
        #                                   output_folder=output_path)

        pass


    def files_to_frames():

        pass

    def delete_video():

        pass

    def delete_frames():

        pass

        
    pass
