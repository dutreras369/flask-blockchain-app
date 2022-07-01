from flask import Blueprint
from controllers.BlockchainController import mine_block, get_chain, is_valid, add_transaction, connect_node, replace_chain

# Creación de enrutador
blockchain_bp = Blueprint('blockchain_bp', __name__)

# Rutas Http 

blockchain_bp.route('/mine_block', methods=['GET'])(mine_block)
blockchain_bp.route('/get_chain', methods=['GET'])(get_chain)
blockchain_bp.route('/is_valid', methods = ['GET'])(is_valid)
blockchain_bp.route('/add_transaction', methods = ['POST'])(add_transaction)
blockchain_bp.route('/connect_node', methods = ['POST'])(connect_node)
blockchain_bp.route('/replace_chain', methods = ['GET'])(replace_chain)



