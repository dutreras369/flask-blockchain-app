from flask import jsonify
import requests
from uuid import uuid4


from models.Blockchain import Blockchain
import sys

# Creación de la Blockchain
blockchain = Blockchain()

# Crear la dirección del nodo en el puerto 5000
node_address = str(uuid4()).replace('-', '')

def mine_block():
  """ Minado de un nuevo bloque """ 

  previous_block = blockchain.get_previous_block()
  previous_proof = previous_block['proof']
  proof = blockchain.proof_of_work(previous_proof)
  previous_hash = blockchain.hash(previous_block)
  blockchain.add_transaction(sender = node_address, receiver = "Joan Amengual", amount = 10)
  block = blockchain.create_block(proof, previous_hash)
  response = {'message'       : '¡Enhorabuena, nuevo bloque minado!', 
              'index'         : block['index'],
              'timestamp'     : block['timestamp'],
              'proof'         : block['proof'],
              'previous_hash' : block['previous_hash'],
              'transactions'  : block['transactions']}
  return jsonify(response), 200

def get_chain():
  """ Obtención de la cadena de bloques al completo """

  response = {'chain'   : blockchain.chain, 
              'length'  : len(blockchain.chain)}
  return jsonify(response), 200

def is_valid():
  """ Comprobación de si la cadena de bloques es válida """

  is_valid = blockchain.is_chain_valid(blockchain.chain)
  if is_valid:
      response = {'message' : 'Todo correcto. La cadena de bloques es válida.'}
  else:
      response = {'message' : 'UPS. La cadena de bloques NO es válida.'}
  return jsonify(response), 200  


def add_transaction():
  """ Añadir una nueva transacción a la cadena de bloques """

  json = requests.get_json()
  transaction_keys = ['sender', 'receiver', 'amount']
  if not all(key in json for key in transaction_keys):
      return 'Faltan algunos elementos de la transacción', 400
  index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
  response = {'message': f'La transacción será añadida al bloque {index}'}
  return jsonify(response), 201
    
# Descentralización de la Cadena de Bloques

# Conectar nuevos nodos
def connect_node():
  json = requests.get_json()
  nodes = json.get('nodes')
  if nodes is None: 
      return 'No hay nodos para añadir', 400
  for node in nodes:
      blockchain.add_node(node)
  response = {'message'     : 'Todos los nodos han sido conectados. La Blockchain de JoanCoins contiene ahora los nodos siguientes: ',
              'total_nodes' : list(blockchain.nodes)}
  return jsonify(response), 201

def replace_chain():
  """ Reemplazar la cadena por la más larga (si es necesario) """

  is_chain_replaced = blockchain.replace_chain()
  if is_chain_replaced:
      response = {'message' : 'Los nodos tenían diferentes cadenas, se ha remplazado por la Blockchain más larga.',
                  'new_chain': blockchain.chain}
  else:
      response = {'message'       : 'Todo correcto. La Blockchain en todos los nodos ya es la más larga.',
                  'actual_chain'  : blockchain.chain}
  return jsonify(response), 200  