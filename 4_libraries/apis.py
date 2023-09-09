import json   # this library comes with Pythom
import requests
import sys

if len(sys.argv) != 2:
    sys.exit('Error, program should have at least one command-line argument')


response = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1]) # Así se hace un API, con ésta librería

#print('\n\nAPI without json library: \n',response.json())   # Así la respuesta del servidor va a estar en formato JSON
# Python converts a JSON with the get function, to a dictionary, that uses almost the same syntax as JSON


print('\n\nAPI with json library: \n',json.dumps(response.json(), indent=2),'\n\n\n')

# Para descomentar éstas líneas, cambiar a limit=1 en la API

ob = response.json()
for r in ob["results"]:
    print(r["trackName"])
