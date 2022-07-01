from routes.front_bp import front
from routes.blockchain_bp import blockchain_bp
from app import app

app.register_blueprint(front)
app.register_blueprint(blockchain_bp)