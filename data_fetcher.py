import os
from dotenv import load_dotenv
import requests

load_dotenv()

def data_fetcher(name):
  URL = f'https://api.api-ninjas.com/v1/animals?name={name}'
  API_KEY = os.getenv('API_KEY')
  print('API ', API_KEY)
  response = requests.get(URL, headers={'X-Api-Key': API_KEY})
  if not response.json():
      return False
  else:
      print('response ', response.json())
      return response.json()
