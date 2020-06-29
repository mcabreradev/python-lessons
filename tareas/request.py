
import requests
import json

# api-endpoint
URL = "https://mcabreradev-pokedex-api.herokuapp.com/pokemons?$limit=1"

r = requests.get(url=URL)

data = r.json()

print(json.dumps(data, indent=2, sort_keys=True))
print(data['limit'])
