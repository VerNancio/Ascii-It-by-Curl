from flask import Flask, request, jsonify

# from .routes import main as main_blueprint
from .controllers import list_controller, stream_controller, upload_controller



def create_app():
        
    app = Flask(__name__)


    # Extensões permitidas de serem serem enviadas como uploads
    ALLOWED_EXTENSIONS: list[str] = ["mp4"]


    # Dicionário contendo todas as rotas e subrotas
    ALL_ROUTES_DICT: dict[dict[list[str]]] = {
        'list': {
            'groups': ['groups', 'ascii_groups', 'all_groups'], 
            'routes': ['routes', 'all_routes'], 
            'all_ascii': ['all_ascii'],
            'allowed_extensions': ['allowed_extensions', 'extensions', 'allowed_uploads']
            },
        'stream': {
            'single': ['single', 'ascii'],
            'group': ['group', 'ascii_group'],
            'random': ['random', 'random_ascii']
        },
        'upload': {
            
        }
    }

    app.config['ALLOWED_EXTENSION'] = ALLOWED_EXTENSIONS
    app.config['ALL_ROUTES_DICT'] = ALL_ROUTES_DICT

    # Tamanho máximo de video/gif a ser enviado
    app.config['MAX_CONTENT_LENGTH'] = 8 * 1000 * 1000


    FILES_FOLDER = 'files'

    UPLOAD_FOLDER = 'uploaded_files'
    FRAMES_FOLDER = 'frames_folder'
    ASCII_FOLDER = 'ascii_folder'

    app.config['FILES_FOLDER'] = FILES_FOLDER

    app.config['UPLOAD_FOLDER'] = f"{FILES_FOLDER}/{UPLOAD_FOLDER}"
    app.config['ASCII_FOLDER'] = f"{FILES_FOLDER}/{ASCII_FOLDER}"
    app.config['FRAMES_FOLDER'] = f"{FILES_FOLDER}/{FRAMES_FOLDER}"


    @app.before_request
    def curl_check():
        user_agent = request.headers.get('User-Agent', '')

        if 'curl' not in user_agent:
            return jsonify({"error": "Tu quase arruínou uma surpresa legal, dá um curl aqui pelo terminal XP"})
        
        
    # Rota '/' inclusa no bp de list
    app.register_blueprint(list_controller.bp)

    app.register_blueprint(stream_controller.bp)
    # app.register_blueprint(stream_controller.bp)


    return app


