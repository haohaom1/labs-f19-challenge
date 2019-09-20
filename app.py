from flask import Flask, escape, url_for
import requests

app = Flask(__name__)


@app.route('/pokemon/<entry>')
def pokemon_identify(entry):
    req = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(entry))
    data = req.json()
    # return '{}\'s profile'.format(escape(entry))
    
    # entered int
    if entry.isdigit():      
        name = data['name']
        return 'The pokemon with id {} is {}'.format(entry, name)
    # entered name
    else:           
        pokemonID = data['id']
        return '{} has id {}'.format(entry, pokemonID)


if __name__ == '__main__':
    app.run()
