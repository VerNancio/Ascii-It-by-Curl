from app import create_app
import sys


# Porta passada como argumento
if len(sys.argv) > 1:
    APP_PORT = sys.argv[1] 
else:
    APP_PORT = '5000'
    

if __name__ == "__main__":

    app = create_app()
    
    app.run(debug=True, port=APP_PORT)