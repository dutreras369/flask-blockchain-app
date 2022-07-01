# Importación de las librerías 
import os
from flask import Flask, render_template
from flask_migrate import Migrate

from routes.front_bp import front
from routes.blockchain_bp import blockchain_bp

# app create
app = Flask(__name__, template_folder="views")

migrate = Migrate(app)

# register routes
app.register_blueprint(front)
app.register_blueprint(blockchain_bp)

# error 500, actualized and execute whit this line
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

if __name__ == '__main__':
    app.debug = True
    app.run()