from flask import Blueprint
from controllers.BlockchainController import mine_block, get_chain, is_valid

# Creación de enrutador
blockchain_bp = Blueprint('blockchain_bp', __name__)

# Rutas Http 
blockchain_bp.route('/mine_block', methods=['GET'])(mine_block)
blockchain_bp.route('/get_chain', methods=['GET'])(get_chain)
blockchain_bp.route('/is_valid', methods = ['GET'])(is_valid)
