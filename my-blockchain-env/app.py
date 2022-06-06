# Importación de las librerías 
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_ngrok import run_with_ngrok

# Crear una aplicación web
# Ejecución de la app con Notebook
app = Flask(__name__)
migrate = Migrate(app)

run_with_ngrok(app)  

# Si se obtiene un error 500, actualizar flask y ejecutar la siguiente línea
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()