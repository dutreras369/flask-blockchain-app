from flask import jsonify
from models.Blockchain import Blockchain
import sys

# Creación de la Blockchain
blockchain = Blockchain()

def mine_block():
  """ Minado de un nuevo bloque """

  previous_block  = blockchain.get_previous_block()
  previous_proof  = previous_block['proof']
  proof           = blockchain.proof_of_work(previous_proof)
  previous_hash   = blockchain.hash(previous_block)
  block           = blockchain.create_block(proof, previous_hash)
  response = {'message'       : '¡Enhorabuena, has minado un nuevo bloque!', 
              'index'         : block['index'],
              'timestamp'     : block['timestamp'],
              'proof'         : block['proof'],
              'previous_hash' : block['previous_hash']}
  return jsonify(response), 200

def get_chain():
  """ Obtención de la Blockchain """
  response = {'chain'   : blockchain.chain, 
              'length'  : len(blockchain.chain)}
  return jsonify(response), 200

def is_valid():
  """ Comprobación si la Blockchain es válida """

  is_valid = blockchain.is_chain_valid(blockchain.chain)
  if is_valid:
      response = {'message' : '¡La cadena de bloques es válida!'}
  else:
      response = {'message' : '¡La cadena de bloques NO es válida!'}
  return jsonify(response), 200  
