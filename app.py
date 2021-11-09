import requests

response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
print(response.json())

# I need to extract the text inside the json response from the API endpoint
