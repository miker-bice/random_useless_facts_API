import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    response.raise_for_status()

    jsonResponse = response.json()
    print(f"""THE RANDOM USELESS FACT: 
            {jsonResponse['text']}""")
    print(f"source: {jsonResponse['source']}")
except HTTPError as http_err:
    print(f'Http error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')


