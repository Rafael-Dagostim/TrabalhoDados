import flask 
from flask import jsonify, request
from pokemon_list import pokemon_list

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/pokemons/all', methods=['GET'])
def list_all_pokemons():
    return jsonify(pokemon_list)

app.run()