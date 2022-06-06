# Importación de las librerías 
import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_ngrok import run_with_ngrok
import os


# app create
app = Flask(__name__)

# execute from notebook
migrate = Migrate(app)

run_with_ngrok(app)  

# error 500, actualized and execute whit this line
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()