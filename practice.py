import requests

api_key = 'ebd9b3d3-a5eb-4a5c-8d00-4293c9e686e4'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)